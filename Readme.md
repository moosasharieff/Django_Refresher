
**For using logic :**

`{* use for / if statement logic here *}`

**For just pasting data :**

`{{ use variable names to paste the data }}`

**Using If Statements in HTML for template tags**
```
{% if access_records %}
	add you logic here
{% else %}
	add you logic here
{% endif %}
```

**Using For Loop in HTML for template tags**
```
{% for ele in access_records %}
    add you logic here
{% endfor %}
```

**Using FormModel to inject data from User Form to Database (Models) directly**
We’ll be using something new called `ModelForm` used for injecting data from Form directly into Models (Database). We can achieve this using a `Meta Class` - A class within a class is called as Meta Class.

**Syntax**
```python
from django import forms
from myapp.models import MyModel

class MyNewForm(forms.ModelForm):
	# Form fields go here
	

	class Meta:
		model = MyModel
		fields = # We see lots of other options here
```

*We can also create our Form based on Model.
Use the below Syntax :*
1. Set it to `“__all__”` : You’re grabbing all the fields from the model and placing it into the form.
    
    ```python
    from django import forms
    from app_two.models import User
    
    class NewUserForm(forms.ModelForm):
        class Meta():
            model = User
            fields = "__all__"	
    ```
    
2. Mention the fields you want to exclude 
    
    ```python
    	class Meta:
    		model = MyModel
    		exclude = ["field1", "field2"]
    ```
    
3. Mention the fields you want to include
    
    ```python
    	class Meta:
    		model = MyModel
    		fields = ("field1", "field2")
    ```
---

#### Different Syntax methods of using URLs in our templates (HTML Files)
Currently using method in HTML File (Static path) <br>
`<a href="basicapp/thankyou"> Thank You </a>`

**Different method Relative URLs can be used in Template tags**
**Option 1:** name="thanku" is in the urls.py file of your application :--> <br>
<a href="{% url 'thanku'%}"> Thank You </a>`

**Suggested Method : Option 2:** This method requires that app_name variable to be created inside the urls.py file! :--> <br>
`<a href="{% url 'app_four_application:relative'%}"> Thank You </a>`

```
Note : 
app_four_application --> is the app_name
relative --> is the var=name in urlpatterns
```
