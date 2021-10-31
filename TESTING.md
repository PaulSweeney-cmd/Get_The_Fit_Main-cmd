
# Production

### Rendering product size:
* Dictionary renders [{ Product Name: Size }] in the size field on the shopping bag page instead of just the size chosen.
### FIX: 
* Appended key/value pair for quantity in bag items context processor else statement - with thanks to scott from Tutor Support @ [Code Institute](https://codeinstitute.net/) for pointing out the typo.
### Quantity input:
* Quantity input box not working when I click on the chevron buttons to increase or decrease product quantity in the shopping bag.
### FIX: 
* Syntax error: When I copied and pasted input box code from my product detail page I didn't include the closing div tag and didn't update value field to {{ item.item_quantity }}.
### Delete Product:
* Delete function not working, print statement in except Exception returns "POST /shopping_bag/delete/26/ HTTP/1.1" 500 0 'extra small'
### FIX: 
* Fixed typo in delete function in views removed [size] from line 63, 93. delete function now works
### Products not deleting in shopping bag
* Delete function not working, print statement in except Exception returns "POST /shopping_bag/delete/26/ HTTP/1.1" 500 0 'extra small'
### FIX: 
* Fixed typo in delete function in views removed [size] from line 63, 93. delete function now works
### Webhooks :
* Payment-intent not working: test webhook charge succeeded but internal server error stated there was an issue with a typo as follows....order = Order.object.create() whereas it should have been order = Order.objects.create().
### FIX: 
* Issue rectified, new endpoint set up and re-tested.
### Webhooks :
* User profile not updating on submit.
### FIX: 
* Syntax error in jinja templating, incorrect syntax for url ( missing })

# User Testing:

## Product deleting and size not showing on shopping bag page whe user updates a quantity

* This was a bug I had major issue trying to fix, despite a tedious amount of time with tutor support, this could not be rectified before my submission deadline. Tutor support did send over some updated code from the boutique ado project. this was looked in to and changes applied with no positive result.



