from GetCourses import GetCourses

from Elastic import Elastic

el = Elastic()

print("server is ready")

query = GetCourses()

print(query)
