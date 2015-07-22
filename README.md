# Easy_phi python client
Python client demonstrates how to work with easy_phi web application. 
- The library of the client implemented in 'easy_phi_client.py' file
- Sample app stored in 'app.py' file



- `base_url` - http address of the Easy_phi_API web application

- `api_token` - Easy_phi_API token
This is in development now. In the future, you will be able to find it in your easy_PHi_API security settings

Running the client
-----------

To get the results, run:

    python app.py <scpi command>

e.g.:

    python app.py RAck:Size?

will return number of slots. By default, command will be broadcasted to all 
modules and will return result from module connected to slot with lowest number.

To see how to specify (host, api token and slot), run program with `--help` 
parameter:

    python app.py --help
    
    
