=========================
django-responsive-viewer
=========================


You Can View your page in different resolution at the same page. it is beneficial for f2e developer

Quick start
-----------

1. Add "django_responsive_viewer" in your INSTALLED_APP

.. code-block:: python

    INSTALLED_APPS = (
        'django_responsive_viewer',
    )

2. set up which url you want to show in responsive viewr

.. code-block:: python

    RESPONSIVE_SPECS = (
        [320, 568],  # iPhone
        [568, 320],  # iPhone
        [768, 1024],  # iPad landscape
        [1024, 768],  # iPad 
        [1366, 768/2],  # notebook
    )

    RESPONSIVE_VIEWER = [
        '/direct_render/sidebar.html',  # this is the url you want to view
    ]


3. of course, you need to setup url

.. code-block:: python

    import django_responsive_viewer.urls
    url(r'^responsive_viewer/', include(django_responsive_viewer.urls)),
 


