# TRAKO

## In progress

Wrapper for Trello api, specified for Mako schedule project. Main goal is to implement functions to interact with board specified for Mako. 

## Functionality
* Tasks for every day can be sent to Trello board (tasks structure is defined by Mako)
* Tasks can be moved inside the Trello board
* Board is overridden every time a new board is created for the day
* Sync updates status of tasks in Mako database  
* Board contains three columns: TO DO, DOING and DONE
* Cards contains data from `mako today` : task, project, subproject, description, time estimate and due data
* Estimation can not be changed in Trello
* Each card in Trello board represents a task:
    * title is description of a task and after last `-` time to work on a task
    * in description are respectively: project name, subproject name and original estimation seperated with new line
    * due date is due date from Mako
* When upload - all tasks go to TODO column

## Functions
* `setup_user_token` - initial run: setup token, create workspace and a board
* `upload_data` - create new board for day and deletes old if exist
* `get_data` - gets data for the tasks from the board

## Update
* save board ID in a data structure
* read all lists names only once