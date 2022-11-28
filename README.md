# odoo15
Working on my Odoo cookbook

I jumped to Chp 16 Owl because of the large changes to web dev in Odoo to Owl.
Creating an OWL component
1.  I do not use the template.xml in views dir.
2.  I used the manifest.py to add the component.js file to the assets_backend
3.  It seems to work, except the component was loaded on top instead of on the bottom.  Not sure why.

Managing user actions in an OWL component
We add a 't-on-<event>' to response to events.
In this example, the event is a 'click'.  It could have been a mouseover.
Triggering will call the method 'OnRemove' which is calling the default this.destroy() fn.