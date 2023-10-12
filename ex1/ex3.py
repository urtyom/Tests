def record_holders(courses, mentors, durations, min, max):
  courses_list = []
  for course, mentor, duration in zip(courses, mentors, durations):
    course_dict = {
          "title": course,
          "mentors": mentor,
          "duration": duration
      }
    courses_list.append(course_dict)
  maxes = []
  minis = []
  for index, duration in enumerate(durations):
    if duration == max:
      maxes.append(index)
    elif duration == min:
      minis.append(index)

  courses_min = []
  courses_max = []
  for id in minis:
    courses_min.append(courses_list[id]["title"]) 
  for id in maxes:
    courses_max.append(courses_list[id]["title"])

  return ", ".join(courses_min), min, ", ".join(courses_max), max
