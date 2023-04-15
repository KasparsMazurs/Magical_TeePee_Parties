from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, PostGallery, PostProducts, BookAParty
from .forms import CommentForm, BookingForm
from django.views.generic import ListView
from django.urls import reverse


class PostList(generic.ListView):
    """
    Create a view to see all posts
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):
    """
    Create a view to see specific post in more details
    """

    def get(self, request, slug, *args, **kwargs):
        # Get all posts with status=1 (i.e., published posts)
        queryset = Post.objects.filter(status=1)

        # Get the post with the specified slug from the queryset
        post = get_object_or_404(queryset, slug=slug)

        # Get all approved comments for the post, sorted by creation date
        comments = post.comments.filter(approved=True).order_by("-created_on")

        # Check if the current user has liked the post
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Get the total number of likes for the post
        total_likes = post.likes.count()

        # Render the post detail template with:
        # the post, comments, liked status,
        # comment form, and total likes as context variables
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
        # Get all posts with status 1 (published) and filter by slug
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        # Get all comments for this post that have been approved and
        # order by creation date
        comments = post.comments.filter(approved=True).order_by("-created_on")

        # Check if the current user has liked the post
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # If the request method is POST, validate the comment form and
        # save the comment
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Set the email and name of the comment to the current user's
            # email and username
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username

            # Create a new comment instance and associate it with
            # the current post
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            # If the form is not valid, create a new, empty form
            comment_form = CommentForm()

        # Render the post detail template with the post,
        # comments, comment form, and other variables
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
    """
    Will show likes for posts
    """
    def post(self, request, slug, *args, **kwargs):
        # Get the post object with the given slug
        # or return 404 page not found error
        post = get_object_or_404(Post, slug=slug)

        # Check if the current user has already liked the post
        if post.likes.filter(id=request.user.id).exists():
            # If the user has already liked the post, remove their like
            post.likes.remove(request.user)
        else:
            # If the user has not liked the post, add their like
            post.likes.add(request.user)

        # Redirect to the post detail page
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class GalleryListView(ListView):
    """
    Will show all galleries
    """
    model = PostGallery
    template_name = 'gallery.html'
    context_object_name = 'post_galleries'

    def get_queryset(self):
        return PostGallery.objects.all()


class SeeGalleryView(generic.DetailView):
    """
    Will show specific galleries in more detail
    """
    model = PostGallery
    template_name = 'see_gallery.html'

    def get_context_data(self, **kwargs):
        # Call the parent implementation of `get_context_data` and
        # get the context dictionary.
        context = super().get_context_data(**kwargs)

        # Add the queryset of images associated with the current object to
        # the context dictionary.
        # Here, `self.object` refers to the current object being
        # displayed in the view.
        # The object has a related manager named `images` that
        # returns a queryset of images.
        context['images'] = self.object.images.all()

        # Return the updated context dictionary.
        return context


class ProductsListView(ListView):
    """
    Will show all Products
    """
    model = PostProducts
    template_name = 'products.html'
    context_object_name = 'post_products'

    def get_queryset(self):
        return PostProducts.objects.all()


class ProductView(generic.DetailView):
    """
    Will show specific Product in more detail
    """
    model = PostProducts
    template_name = 'products_detail.html'

    def get_context_data(self, **kwargs):
        # Call the parent class's get_context_data method
        # to get the initial context
        context = super().get_context_data(**kwargs)

        # Get all the images related to the object
        # and add them to the context
        context['images'] = self.object.images.all()

        # Return the updated context
        return context


class ContactUsView(View):
    """
    Will render contact_us.html
    """
    template_name = 'contact_us.html'

    def get(self, request):
        return render(request, self.template_name)


class AboutUsView(View):
    """
    Will render about_us.html
    """
    template_name = 'about_us.html'

    def get(self, request):
        return render(request, self.template_name)


class BookAPartyView(View):
    """
    Will render book_a_party.html
    """
    template_name = 'book_a_party.html'

    def get(self, request):
        # Create a new BookingForm instance
        form = BookingForm()

        # Define the context dictionary with the form as a value
        context = {'form': form}

        # Render the booking form template with the context data
        return render(request, self.template_name, context)

    def post(self, request):
        form = BookingForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            # Create a new instance of the BookAParty model and populate
            # its fields with the form data
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

            # Set the user who submitted the party as the host
            party.host = request.user

            # Save the new party instance to the database
            party.save()

            # Redirect the user to the submitted parties page
            return redirect(reverse('submitted_parties'))

        context = {'form': form}
        return render(request, self.template_name, context)


def submitted_parties(request):
    # Fetch parties submitted by the current user
    parties = BookAParty.objects.filter(host=request.user)

    # Create a context dictionary with the parties queryset
    context = {'parties': parties}

    # Render the submitted_parties.html template with the context dictionary
    return render(request, 'submitted_parties.html', context)


class EditPartyView(View):
    """
    Create a view for edit party
    """
    template_name = 'edit_party.html'

    def get(self, request, order_nr):
        # Combine the order number with a string to match
        # the format used in the database
        order_nr = 'order-' + order_nr

        # Retrieve the party from the database with the given order number,
        # or return a 404 error if it doesn't exist
        party = get_object_or_404(BookAParty, order_nr=order_nr)

        # Create a form for booking and prepopulate its fields with
        # the data from the party instance
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

        # Define the context variables that will be passed to the template
        context = {'form': form, 'order_nr': order_nr}

        # Render the booking form template with the prepopulated form fields
        # and the order number
        return render(request, self.template_name, context)

    def post(self, request, order_nr):
        # Construct the order number from the URL parameter
        order_nr = 'order-' + order_nr

        # Retrieve the party booking using the order number
        party = get_object_or_404(BookAParty, order_nr=order_nr)

        # Populate the booking form with the party details
        form = BookingForm(request.POST, instance=party)

        # Checks if the 'delete' button was clicked 
        # and if it was, it deletes the corresponding party object
        if 'delete' in request.POST:
            party.delete()
            return redirect(reverse('submitted_parties'))

        # If the form is valid, save the booking and
        # redirect to the submitted parties page
        if form.is_valid():
            # Save the form data to the party object
            party = form.save(commit=False)
            party.approved = False
            form.save()
            return redirect('submitted_parties')

        # If the form is not valid, render the form again with error messages
        context = {'form': form, 'order_nr': order_nr}
        return render(request, self.template_name, context)


class DeletePartyView(View):
    """
    Allows to delete submitted party
    """
    def post(self, request, party_id):
        # Retrieve the party object using its ID,
        # or return a 404 error if it doesn't exist
        party = get_object_or_404(BookAParty, id=party_id)

        # Call the `delete()` method on the party object
        # to delete it from the database
        party.delete()

        # Redirect to the submitted parties page using the `reverse()`
        # function to look up the URL by name
        return redirect(reverse('submitted_parties'))
