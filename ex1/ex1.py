def uniq_name(mentors):
  all_list = []
  for m in mentors:
    all_list += m

  all_names_list = []
  for mentor in all_list:
    name = mentor.split(' ')[0]
    all_names_list.append(name)
      
  unique_names = set(all_names_list)
  all_names_sorted = sorted(list(unique_names))
  return ", ".join(all_names_sorted[:3])
