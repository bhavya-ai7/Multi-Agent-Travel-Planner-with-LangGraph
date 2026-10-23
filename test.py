from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights

# res=tavily_search("Best hotels in USA")
# print(res)

res = search_flights("Plan a 7 days BLR trip from US")
print(res)