# Setup Environment

## Create virtual ENV

```bash
python3 -m venv ../venv
```

## Activate VENV
```bash
source ../venv/bin/activate
```

## Install Dependencies
```bash
pip install -r requirements.txt
```

**notes**: `SQLAlchemy` is required to be version `SQLAlchemy==1.4.0`

As of version `0.15.49`, `Great Expectations` does not supports `SQLAlchemy>=2.0.0`