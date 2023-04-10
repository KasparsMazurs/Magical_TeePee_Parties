from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, PostGallery, PostProducts, BookAParty
from .forms import CommentForm, BookingForm
from django.views.generic import ListView
from django.urls import reverse


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        total_likes = post.likes.count()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
                "total_likes": total_likes,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):  
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class GalleryListView(ListView):
    model = PostGallery
    template_name = 'gallery.html'
    context_object_name = 'post_galleries'

    def get_queryset(self):
        return PostGallery.objects.all()


class SeeGalleryView(generic.DetailView):
    model = PostGallery
    template_name = 'see_gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = self.object.images.all()
        return context


class ProductsListView(ListView):
    model = PostProducts
    template_name = 'products.html'
    context_object_name = 'post_products'

    def get_queryset(self):
        return PostProducts.objects.all()


class ProductView(generic.DetailView):
    model = PostProducts
    template_name = 'products_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = self.object.images.all()
        return context


class ContactUsView(View):
    template_name = 'contact_us.html'

    def get(self, request):
        return render(request, self.template_name)


class AboutUsView(View):
    template_name = 'about_us.html'

    def get(self, request):
        return render(request, self.template_name)


class BookAPartyView(View):
    template_name = 'book_a_party.html'

    def get(self, request):
        form = BookingForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = BookingForm(request.POST)
        if form.is_valid():
            # Create a new instance of the BookAParty model and populate its fields with the form data
            party = BookAParty()
            party.party_theme = form.cleaned_data['party_theme']
            party.balloons = form.cleaned_data['balloons']
            party.bouncy_castle = form.cleaned_data['bouncy_castle']
            party.kids_age = form.cleaned_data['kids_age']
            party.number_of_teepees = form.cleaned_data['number_of_teepees']
            party.street = form.cleaned_data['street']
            party.city = form.cleaned_data['city']
            party.county = form.cleaned_data['county']
            party.eircode = form.cleaned_data['eircode']
            party.date = form.cleaned_data['date']
            party.email = form.cleaned_data['email']
            party.phone_number = form.cleaned_data['phone_number']
            party.additional_info = form.cleaned_data['additional_info']
            party.price = 0.0
            party.host = request.user
            party.save()

            return redirect(reverse('home'))
        context = {'form': form}
        return render(request, self.template_name, context)


def submitted_parties(request):
    # Fetch parties submitted by the current user
    parties = BookAParty.objects.filter(host=request.user)
    context = {'parties': parties}
    return render(request, 'submitted_parties.html', context)


class EditPartyView(View):
    template_name = 'edit_party.html'

    def get(self, request, order_nr):
        order_nr = 'order-' + order_nr
        party = get_object_or_404(BookAParty, order_nr=order_nr)

        # Create a form and populate its fields with the data from the party instance
        form = BookingForm(initial={
            'party_theme': party.party_theme,
            'balloons': party.balloons,
            'bouncy_castle': party.bouncy_castle,
            'kids_age': party.kids_age,
            'number_of_teepees': party.number_of_teepees,
            'street': party.street,
            'city': party.city,
            'county': party.county,
            'eircode': party.eircode,
            'date': party.date,
            'email': party.email,
            'phone_number': party.phone_number,
            'additional_info': party.additional_info
        })

        context = {'form': form, 'order_nr': order_nr}
        return render(request, self.template_name, context)

    def post(self, request, order_nr):
        order_nr = 'order-' + order_nr
        party = get_object_or_404(BookAParty, order_nr=order_nr)
        form = BookingForm(request.POST, instance=party)
        if form.is_valid():
            form.save()
            return redirect('submitted_parties')
        context = {'form': form, 'order_nr': order_nr}
        return render(request, self.template_name, context)