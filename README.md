# matrix_clockwise_traverse
The Django project to get a matrix from server using API, traverse it clockwise, and return a list of its values.

##
The input matrix can be any size but should be in format:
'''
+-----+-----+-----+-----+
|  10 |  20 |  30 |  40 |
+-----+-----+-----+-----+
|  50 |  60 |  70 |  80 |
+-----+-----+-----+-----+
|  90 | 100 | 110 | 120 |
+-----+-----+-----+-----+
| 130 | 140 | 150 | 160 |
+-----+-----+-----+-----+
'''

## Used stack
1. Django
2. HTTPX
3. Django-ninja

Install requirements before using
'''
pip install -r requirements.txt
'''

## Using
To get matrix from server and return list of its values use endpoint /api/get_matrix/ + url. Example:
'''
http://127.0.0.1:8000/api/get_matrix/?url=https://raw.githubusercontent.com/Real-Estate-THE-Capital/python-assignment/main/matrix.txt
'''


