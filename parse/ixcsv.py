import csv

class CSVRow:

  def __init__(self, header, row):
    self._header = header
    self._row = row

  def __getitem__(self, key):
    return self._row[self._header._getIndex(key)]

  def __setitem__(self, key, value):
    self._row[self._header._getIndex(key)] = value

class CSVFile:

  def __init__(self, filepath):
    csvfile = csv.reader(open(filepath))

    self._rows = []
    self._headers = {}

    for i, row in enumerate(csvfile):
      if i == 0:
        for j, h in enumerate(row):
          self._headers[h] = j
      else:
        self._rows.append(CSVRow(self, row))
  
  def _getIndex(self, heading):
    return self._headers[heading]

  def __getitem__(self, key):
    return self._rows[key]
  
  def rows(self):
    return iter(self._rows)

  def print(self):
    print(self._headers)
    for row in self._rows:
      print(row)