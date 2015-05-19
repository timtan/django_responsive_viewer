#Responsive style guide

Show Specific URL with iframe settings


## Usage

1. install
   * pip install
   * add 'django_responsive_viewer' to your INSTALLED_APPS

2. modify your projects urls.py

```py
    url(r'^responsive_viewer/', include(django_responsive_viewer.urls)),
```    
 
3. Add the following settings

```python
	RESPONSIVE_VIEWER = (
	    'direct_render/hello.html',
	    'direct_render/base_layout.html',
	)
```

4. visit the page 

	http://localhost:8000/responsive_viewer/







