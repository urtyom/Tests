import pytest
from ex1 import uniq_name
from ex2 import uniq_name_3
from ex3 import record_holders
from info import courses, mentors, durations, min, max


@pytest.mark.parametrize(
  "courses, mentors, durations, min, max",
  [
    (courses, mentors, durations, min, max)
  ]
)

def test_uniq_name():
  expected = 'Адилет, Азамат, Александр'
  result = uniq_name(mentors)
  assert result == expected

def test_uniq_name_3(mentors):
  expected = 'Александр: 10 раз(а), Евгений: 5 раз(а), Максим: 4'
  result = uniq_name_3(mentors)
  assert result == expected

def test_record_holders(courses, mentors, durations, min, max):
  expected = ('Python-разработчик с нуля',
              12,
              'Fullstack-разработчик на Python, Frontend-разработчик с нуля',
              20)
  result = record_holders(courses, mentors, durations, min, max)
  assert result == expected
