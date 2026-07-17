# Logging & Monitoring Documentation

## Overview

The project includes a logging system that records API requests, prediction activities, and application errors. Logging helps monitor API usage, troubleshoot issues, and audit prediction events.

---

# Logging Components

The system uses three dedicated loggers.

| Logger | File |
|---------|------|
| API Logger | logs/api.log |
| Prediction Logger | logs/prediction.log |
| Error Logger | logs/error.log |

---

# API Request Logging

Every incoming API request is logged.

Information Recorded

- HTTP Method
- Request Path
- Client IP Address
- Response Status Code
- Processing Time

Example

```
2026-07-18 14:21:15 | INFO |
POST | /predict | 127.0.0.1 | 200 | 0.0832 sec
```

---

# Prediction Logging

Every successful prediction is recorded.

Information Recorded

- Prediction Result
- Churn Probability
- Customer Cluster
- Generated Recommendations

Example

```
Prediction      : Yes
Probability     : 0.8642
Cluster         : 2

Recommendations:
- Offer discount for yearly contract.
- Recommend Tech Support service.
- Recommend Online Security service.
```

---

# Error Logging

Unexpected errors are automatically logged.

Information Recorded

- Error Message
- Exception Type
- Complete Stack Trace

Example

```
Prediction Error

Traceback (most recent call last):

NameError: name 'abc' is not defined
```

---

# Log Directory

```
logs/

├── api.log
├── prediction.log
└── error.log
```

---

# Benefits

- API Monitoring
- Debugging Support
- Prediction Auditing
- Error Tracking
- Production Monitoring
- Faster Issue Resolution