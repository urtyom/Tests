def uniq_name_3(mentors):
  all_list = []
  for m in mentors:
    all_list += m

  all_names_list = []
  for mentor in all_list:
    name = mentor.split(' ')[0]
    all_names_list.append(name)

  unique_names = set(all_names_list)

  popular = []
  for name in unique_names:
    popular.append([name, all_names_list.count(name)])

  popular.sort(key=lambda x:x[1], reverse=True)

  top_3 = popular[: 3]
  top_str = []
  for name, count in top_3:
    top_str.append(name + ': ' + str(count))

  return " раз(а), ".join(top_str)
