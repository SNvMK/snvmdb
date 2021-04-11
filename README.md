# snvmdb

This is the simplest database tool in world! It is written on python and using JSON as data format

## Installation

From PyPi:

`python -m pip install snvmdb`

Cloning from GitHub:

```none
git clone https://github.com/SNvMK/snvmdb.git
cd snvmdb
python -m pip install .
```

Downloading wheel from Releases on GitHub:

`python -m pip install snvmdb-x.x.x-none-any.whl`

## Use

Initialize an empty database

```py
import snvmdb

db = snvmdb.SnvmDB('data.db')
```

Add text value to DB:

```py
db.add('amogus', 'ayy')
```

Add hash-table to DB:

```py
db.add('pog', {})
```

Add pair to created hash-table:

```py
db.append_hash('pog', 'ayy', 'lmao')
```
