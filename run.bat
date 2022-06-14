pytest -v -m "sanity" --html=Reports\GroupedReports21.html testCases/
rempytest -v -m "sanity and regression" --html=Reports\GroupedReports.html testCases/
rempytest -v -m "regression" --html=Reports\GroupedReports.html testCases/
rempytest -v -m "sanity or regression" --html=Reports\GroupedReports.html testCases/
rempytest -v -m "vinsd" --html=Reports\GroupedReports.html testCases/