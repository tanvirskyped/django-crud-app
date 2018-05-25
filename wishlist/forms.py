from django import forms

class WishForm(forms.Form):
    text = forms.CharField(max_length=40,
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Enter wish e.g. Delete junk files', 'aria-label' : 'Wishlist', 'aria-describedby' : 'add-btn'}
        ))
