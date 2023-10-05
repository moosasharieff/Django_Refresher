
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
