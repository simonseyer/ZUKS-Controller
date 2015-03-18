# dynamic-backdrop

`dynamic-backdrop` creates a backdrop around a target element.
This could be useful to hilight an specific part of the website by fading
out anything around.

This component also works for nested webcomponents, because it does not rely
on the `z-index` css property to move a part of the website above the backdrop.
It instead creates multiple backdrops around the target.

The backdrop is restricted to the host element. This allows to just hilight a
sub-part of a specific area on the website. 

##### Example

    <dynamic-backdrop></dynamic-backdrop>

##### Known issues

1. Position of the backdrop is not updated, when `host` or `target` are moved
1. Position of the backdrop is not updated on scroll
1. Browser support has to be checked

See the [component page](http://Eldorado234.github.io/dynamic-backdrop) for more information.
