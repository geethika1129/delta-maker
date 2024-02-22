# Daas-Delta-Maker-Service

## Cargo.toml
- use workspace
- add all crates in membets
- include all dependencies
  
## Crates

### oxbow
Present in rust package registry

### Deltaops
Used to create or append table and add checkpoints

- check for version,if its new,add it in
- add a checkpoint after every 10 tables
- if same version table comes in, create checkpoint

### main.rs
- Include all dependencies
- Create new instances of each of joinset, tablemap, config, queue service client, queue client
- Record the start time using chrono
- get the concurrent tasks length
- for each task, create new queue client and table map clone
- Create new thread and pass in to process_queue function
- if theres a result, add it to joinset
- print table details and process tables
- else sleep
- check for profiling time and if profiling time is more break the lop and stop the process
- clean up for next ru and record the stop time

#### get_concurrent_tasks_len
- record max tasks and finally return the no of calls
- record approximate msg count from the response, if approxmsgcount is 0 then numcalls=0
- Check the number of calls based on maximum messages from call

#### process_queue
- get the messages from queue client
- response
- find avg call duration
- if messages are empty need not process
- else keep track of duratio with start time and end time
- find the avg

#### process_tables

