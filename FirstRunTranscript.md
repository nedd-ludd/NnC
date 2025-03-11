User Prompt

"I'm thinking about going out for lunch next Tuesday with John, can you book it in my calendar?"More info needed:

	'Sure, I can help you with that. Could you please provide me with the specific time and location for the lunch so I can create the event in your calendar?'

"I'm thinking about going out for lunch next Tuesday with John as 12mid-day at carlucios, can you book it in my calendar?"
	More info needed:

	"For me to create this event, could you confirm the duration of your lunch? If you don't have a specific end time in mind, a typical lunch could be scheduled for 1 hour."

"I'm thinking about going out for lunch next Tuesday with John as 12mid-day for one hour at carlucios, can you book it in my calendar?"

There was enough info at that point but error with tools:	  
File "c:\Users\natha\Desktop\NnC\src\ai_int.py", line 97, in handle_run
  File "c:\Users\natha\Desktop\NnC\src\ai_int.py", line 97, in handle_run
    tool_calls = run_status.required_action.tool_calls
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "c:\Users\natha\.virtualenvs\NnC-scTYp6Mf\Lib\site-packages\pydantic\main.py", line 891, in __getattr__
    raise AttributeError(f'{type(self).__name__!r} object has no attribute {item!r}')
AttributeError: 'RequiredAction' object has no attribute 'tool_calls'
PS C:\Users\natha\Desktop\NnC>

Subsequent sessionsn worked.