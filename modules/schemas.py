LIST_SCHEMA = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "token": {
      "type": "string"
    }
  },
  "required": [
    "token"
  ]
}

ADD_SCHEMA = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "token": {
      "type": "string"
    },
    "day": {
      "type": "string"
    },
    "time": {
      "type": "string"
    },
    "text": {
      "type": "string"
    },
    "img": {
      "type": "string"
    }
  },
  "required": [
    "token",
    "day",
    "time"
  ]
}