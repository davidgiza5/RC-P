#definire coduri-MethodeCodes


def enum(**enums):
    return type('Enum', (), enums)


def CoapResponseCode(class_, detail):
    return ((class_ << 5) | (detail))

COAP_TYPE = enum(
    COAP_CON=0,
    COAP_NONCON=1,
    COAP_ACK=2,
    COAP_RESET=3
)

COAP_METHOD = enum(
    COAP_EMPTY=0,
    COAP_GET=1,
    COAP_POST=2,
    COAP_PUT=3,
    COAP_DELETE=4
)

COAP_RESPONSE_CODE = enum(
    COAP_CREATED=[2,1],
    COAP_DELETED=[2, 2],
    COAP_VALID=[2, 3],
    COAP_CHANGED=[2, 4],
    COAP_CONTENT=[2, 5],
    COAP_BAD_REQUEST=[4, 0]
)


COAP_DEFAULT = enum(
    PORT = 5006,
    VERSION = 2,
    TOKENL = 4,
    BUFFER_MAX_SIZE = 1024,
    AKC_TIMEOUT = 2,
    AKC_RANDOM_FACTOR = 1.5,
    MAX_RETRANSMIT = 5,
    TIMEOUT = 2
)