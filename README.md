# Easy_phi python client
Python client demonstrates how to work with easy_phi web application. 
- The library of the client implemented in 'easy_phi_client.py' file
- Sample app stored in 'app.py' file


Setup
----

Get the code:

`git clone git@github.com:QuantumCMU/easy_phi_python.git`

In order to adjust setting edit the following file:

`settings.py`

Following settings available:

- `base_url` - http address of the Easy_phi_API web application

- `api_token` - Easy_phi_API token
This is in development now. In the future, you will be able to find it in your easy_PHi_API security settings

Running the client
-----------

To get the results, run:

    python app.py

Available parameters:

- `slot -s` - number of the slot in which particular module is connected (0 by default)

- `scpi_command -scpi` - particular scpi command that will be sent to the module
This is in development now. In the future, you will be able to find it in your easy_PHi_API security settings

Example of running the client with the parameters:

    python app.py -s 3 -scpi '*IDN?'
