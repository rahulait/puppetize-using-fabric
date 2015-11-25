# puppetize-using-fabric
This project is to automate the task of handling puppet run on all the controller + compute nodes.

It relies on the fabric library to support handling the execution of tasks on the remote nodes.
Passwordless SSH is set up manually between the nodes and the node from where this program is executed. 
Else, one can configure to use password based authentication and can automate the login process with few tweaks.

To run the program, one needs to first install fabric module. This can be done using:-
> bash$ sudo apt-get install fabric

You need to create a settings.ini file similar to template_settings.ini with values filled in it.
One can follow the examples to figure out what values needs to be set in settings.ini file.

Once the configuration is done, the code can be executed using fab command.
> bash$ fab \<methodname\>

The syntax of execution is similar to how programs written using fabric library are executed. 
One can look at the documentation of fabric library to get more information on how to write the program.
