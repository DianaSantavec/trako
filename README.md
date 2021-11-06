# TRAKO

## In progress

Wrapper for Trello api, specified for Mako schedule project. Main goal is to implement functions to interact with boards. 

## Functionality
* Tasks for every day can be sent to Trello board (tasks structure is defined by Mako)
* Tasks can be moved inside the Trello board
* Board is overridden every time board is created for a new day
* Sync updates status of tasks in Mako database  
* Board contains three columns: TODO, DOING and DONE
* Cards contains data from `mako today` : task, project, subproject, description, time estimate and due data

## Functions
* `setup_user_token` - initial run: setup token, create board
* `upload_data` - create new board for day and deletes old if exist
* `get_data` - gets data for the tasks from the board