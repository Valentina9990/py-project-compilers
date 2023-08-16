def createTaskPlanner():
  #Tasks list
  tasks = []

  #Add task
  def addTask(task):
    task['completed'] = False
    tasks.append(task)

  #Remove task
  def removeTask(value):
    for task in tasks:
      if task['id'] == value or task['name'] == value:
        tasks.remove(task)
        break

  #Get tasks
  def getTasks():
    return tasks

  #Get pending tasks
  def getPendingTasks():
    return [task for task in tasks if not task['completed']]

  #Get completed tasks
  def getCompletedTasks():
    return [task for task in tasks if task['completed']]

  #Mark task as completed
  def markTaskAsCompleted(value):
    for task in tasks:
      if task['id'] == value or task['name'] == value:
        task['completed'] = True
        break

  #Get sorted tasks by priority
  def getSortedTasksByPriority():
    return sorted(tasks, key=lambda task: task['priority'])

  #Filter tasks by tag
  def filterTasksByTag(tag):
    return [task for task in tasks if tag in task['tags']]

  #Update task
  def updateTask(taskId, updates):
    for task in tasks:
      if task['id'] == taskId:
        for key, value in updates.items():
          task[key] = value
        break

  #Return functions (Dictionary)
  return {
    'addTask': addTask,
    'removeTask': removeTask,
    'getTasks': getTasks,
    'getPendingTasks': getPendingTasks,
    'getCompletedTasks': getCompletedTasks,
    'markTaskAsCompleted': markTaskAsCompleted,
    'getSortedTasksByPriority': getSortedTasksByPriority,
    'filterTasksByTag': filterTasksByTag,
    'updateTask': updateTask,
  }

def print_dictionaries(dictionaries):
  for dictionary in dictionaries:
    for key, value in dictionary.items():
      print(key, "=", value)
    print()

