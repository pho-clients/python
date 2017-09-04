# pho_client.DefaultApi

All URIs are relative to *https://virtserver.swaggerhub.com/phonetworks/server-rest/1.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_attribute**](DefaultApi.md#add_attribute) | **POST** /{uuid}/attribute/{key} | updates (or creates) an attribute
[**del_attribute**](DefaultApi.md#del_attribute) | **DELETE** /{uuid}/attribute/{key} | deletes an attribute
[**del_entity**](DefaultApi.md#del_entity) | **DELETE** /{uuid} | deletes an entity
[**get_all_edges**](DefaultApi.md#get_all_edges) | **GET** /{uuid}/edges/all | retrieves the edges of a node
[**get_attribute**](DefaultApi.md#get_attribute) | **GET** /{uuid}/attribute/{key} | retrieves the value of an entity attribute
[**get_attributes**](DefaultApi.md#get_attributes) | **GET** /{uuid}/attributes | retrieves the existing attribute keys of an entity (edge or node)
[**get_edge**](DefaultApi.md#get_edge) | **GET** /edge/{uuid} | retrieves an edge
[**get_edge_getters**](DefaultApi.md#get_edge_getters) | **GET** /{uuid}/edges/getters | retrieves the edge getter methods of a node
[**get_edge_setters**](DefaultApi.md#get_edge_setters) | **GET** /{uuid}/edges/setters | retrieves the edge setter methods of a node
[**get_founder**](DefaultApi.md#get_founder) | **GET** /founder | retrieves the Graph Founder
[**get_graph**](DefaultApi.md#get_graph) | **GET** /graph | retrieves the main Graph
[**get_incoming_edges**](DefaultApi.md#get_incoming_edges) | **GET** /{uuid}/edges/in | retrieves the incoming edges of a node
[**get_node**](DefaultApi.md#get_node) | **GET** /{uuid} | retrieves a node
[**get_node_edge**](DefaultApi.md#get_node_edge) | **GET** /{uuid}/{edge} | edge getter
[**get_outgoing_edges**](DefaultApi.md#get_outgoing_edges) | **GET** /{uuid}/edges/out | retrieves the outgoing edges of a node
[**get_space**](DefaultApi.md#get_space) | **GET** /space | retrieves the Space
[**get_type**](DefaultApi.md#get_type) | **GET** /{uuid}/type | fetches entity type
[**make_actor**](DefaultApi.md#make_actor) | **POST** /actor | creates an Actor object
[**make_edge**](DefaultApi.md#make_edge) | **POST** /{uuid}/{edge} | creates an edge
[**set_attribute**](DefaultApi.md#set_attribute) | **PUT** /{uuid}/attribute/{key} | updates (or creates) an attribute


# **add_attribute**
> InlineResponse2004 add_attribute(value=value)

updates (or creates) an attribute

Works with all entities, including nodes and edges. Given its key, updates an  attribute value, or creates it, if it doesn't yet exist. 

### Example 
```python
from __future__ import print_statement
import time
import pho_client
from pho_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pho_client.DefaultApi()
value = 'value_example' # str | The value to update the key with. (optional)

try: 
    # updates (or creates) an attribute
    api_response = api_instance.add_attribute(value=value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| The value to update the key with. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **del_attribute**
> InlineResponse2004 del_attribute()

deletes an attribute

Works with all entities, including nodes and edges. Given its key, deletes an  attribute. 

### Example 
```python
from __future__ import print_statement
import time
import pho_client
from pho_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pho_client.DefaultApi()

try: 
    # deletes an attribute
    api_response = api_instance.del_attribute()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->del_attribute: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **del_entity**
> del_entity()

deletes an entity

Works with all entities, including nodes and edges.  

### Example 
```python
from __future__ import print_statement
import time
import pho_client
from pho_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pho_client.DefaultApi()

try: 
    # deletes an entity
    api_instance.del_entity()
except ApiException as e:
    print("Exception when calling DefaultApi->del_entity: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_edges**
> InlineResponse2003 get_all_edges(uuid)

retrieves the edges of a node

By passing in a node ID, you can fetch all the edges of the node in question; including incoming and outgoing. 

### Example 
```python
from __future__ import print_statement
import time
import pho_client
from pho_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pho_client.DefaultApi()
uuid = 'uuid_example' # str | The node ID

try: 
    # retrieves the edges of a node
    api_response = api_instance.get_all_edges(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_all_edges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The node ID | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attribute**
> str get_attribute(uuid, key)

retrieves the value of an entity attribute

Attribute key must be case-sensitive. 

### Example 
```python
from __future__ import print_statement
import time
import pho_client
from pho_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pho_client.DefaultApi()
uuid = 'uuid_example' # str | The node ID
key = 'key_example' # str | The attribute key

try: 
    # retrieves the value of an entity attribute
    api_response = api_instance.get_attribute(uuid, key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The node ID | 
 **key** | **str**| The attribute key | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attributes**
> list[str] get_attributes(uuid)

retrieves the existing attribute keys of an entity (edge or node)

Attribute keys are case-sensitive, and they will be listed in an array. 

### Example 
```python
from __future__ import print_statement
import time
import pho_client
from pho_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pho_client.DefaultApi()
uuid = 'uuid_example' # str | The node ID

try: 
    # retrieves the existing attribute keys of an entity (edge or node)
    api_response = api_instance.get_attributes(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The node ID | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_edge**
> Edge get_edge(uuid)

retrieves an edge

By passing in an ID, you can search for available edges in the system.  

### Example 
```python
from __future__ import print_statement
import time
import pho_client
from pho_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pho_client.DefaultApi()
uuid = 'uuid_example' # str | The edge ID

try: 
    # retrieves an edge
    api_response = api_instance.get_edge(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_edge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The edge ID | 

### Return type

[**Edge**](Edge.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_edge_getters**
> list[str] get_edge_getters(uuid)

retrieves the edge getter methods of a node

By passing in a node UUID that exists in the database, you can fetch  the edge getter methods of the node in question. 

### Example 
```python
from __future__ import print_statement
import time
import pho_client
from pho_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pho_client.DefaultApi()
uuid = 'uuid_example' # str | The node ID

try: 
    # retrieves the edge getter methods of a node
    api_response = api_instance.get_edge_getters(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_edge_getters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The node ID | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_edge_setters**
> list[str] get_edge_setters(uuid)

retrieves the edge setter methods of a node

By passing in a node UUID that exists in the database, you can fetch  the edge setter methods of the node in question. These setters may or  may not be formative. If they are formative, a new node is created in result. 

### Example 
```python
from __future__ import print_statement
import time
import pho_client
from pho_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pho_client.DefaultApi()
uuid = 'uuid_example' # str | The node ID

try: 
    # retrieves the edge setter methods of a node
    api_response = api_instance.get_edge_setters(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_edge_setters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The node ID | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_founder**
> InlineResponse200 get_founder()

retrieves the Graph Founder

The Founder must be a \\Pho\\Framework\\Actor object.  This method returns the object type as well as object ID. 

### Example 
```python
from __future__ import print_statement
import time
import pho_client
from pho_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pho_client.DefaultApi()

try: 
    # retrieves the Graph Founder
    api_response = api_instance.get_founder()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_founder: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_graph**
> InlineResponse2001 get_graph()

retrieves the main Graph

The Graph must be a \\Pho\\Lib\\Graph\\SubGraph and \\Pho\\Framework\\Graph object.  This method returns the object type as well as object ID. The Graph contains all nodes and edges in the system.  Though it is contained by Space, its one and only container. 

### Example 
```python
from __future__ import print_statement
import time
import pho_client
from pho_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pho_client.DefaultApi()

try: 
    # retrieves the main Graph
    api_response = api_instance.get_graph()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_graph: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_incoming_edges**
> list[NodeEdge] get_incoming_edges(uuid)

retrieves the incoming edges of a node

By passing in a node ID, you can fetch  the incoming edges of the node in question. 

### Example 
```python
from __future__ import print_statement
import time
import pho_client
from pho_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pho_client.DefaultApi()
uuid = 'uuid_example' # str | the node ID

try: 
    # retrieves the incoming edges of a node
    api_response = api_instance.get_incoming_edges(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_incoming_edges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| the node ID | 

### Return type

[**list[NodeEdge]**](NodeEdge.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node**
> Node get_node(uuid)

retrieves a node

By passing in an ID, you can search for available nodes in the system. Please note, this function will not return edges. This method  is  reserved for nodes only.  

### Example 
```python
from __future__ import print_statement
import time
import pho_client
from pho_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pho_client.DefaultApi()
uuid = 'uuid_example' # str | The node ID

try: 
    # retrieves a node
    api_response = api_instance.get_node(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The node ID | 

### Return type

[**Node**](Node.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_edge**
> list[str] get_node_edge(uuid, edge)

edge getter

Fetches edge results, whether as edge IDs or node IDs, depending on edge's characteristics.  

### Example 
```python
from __future__ import print_statement
import time
import pho_client
from pho_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pho_client.DefaultApi()
uuid = 'uuid_example' # str | The node ID
edge = 'edge_example' # str | The edge getter label

try: 
    # edge getter
    api_response = api_instance.get_node_edge(uuid, edge)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_node_edge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The node ID | 
 **edge** | **str**| The edge getter label | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outgoing_edges**
> list[NodeEdge] get_outgoing_edges(uuid)

retrieves the outgoing edges of a node

By passing in a node ID, you can fetch  the outgoing edges of the node in question. 

### Example 
```python
from __future__ import print_statement
import time
import pho_client
from pho_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pho_client.DefaultApi()
uuid = 'uuid_example' # str | the node ID

try: 
    # retrieves the outgoing edges of a node
    api_response = api_instance.get_outgoing_edges(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_outgoing_edges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| the node ID | 

### Return type

[**list[NodeEdge]**](NodeEdge.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_space**
> InlineResponse2002 get_space()

retrieves the Space

The Space must be a \\Pho\\Lib\\Graph\\Graph object.  This method returns the object type as well as object uuid. Space always comes with the nil ID;  00000000000000000000000000000000, and under normal circumstances its class is always Pho\\Kernel\\Standards\\Space 

### Example 
```python
from __future__ import print_statement
import time
import pho_client
from pho_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pho_client.DefaultApi()

try: 
    # retrieves the Space
    api_response = api_instance.get_space()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_space: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_type**
> str get_type(uuid)

fetches entity type

Possible values are; \"Space\", \"Node\", \"Graph Node\", \"Graph\", \"Actor Node\" \"Object Node\", \"Edge\", \"Read Edge\", \"Write Edge\", \"Subscribe Edge\", \"Mention Edge\", \"Unidentified\". 

### Example 
```python
from __future__ import print_statement
import time
import pho_client
from pho_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pho_client.DefaultApi()
uuid = 'uuid_example' # str | the node

try: 
    # fetches entity type
    api_response = api_instance.get_type(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| the node | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **make_actor**
> str make_actor(param1=param1)

creates an Actor object

Fetches whatever set as \"default_object\"=>\"actor\" while determining what Actor object to construct. If it doesn't exist, uses \"default_object\"=>\"founder\" class. Otherwise fails. 

### Example 
```python
from __future__ import print_statement
import time
import pho_client
from pho_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pho_client.DefaultApi()
param1 = 'param1_example' # str | Actor constructor argument. More parameters may be passed via param2, param3 ... param50.  (optional)

try: 
    # creates an Actor object
    api_response = api_instance.make_actor(param1=param1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->make_actor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **param1** | **str**| Actor constructor argument. More parameters may be passed via param2, param3 ... param50.  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **make_edge**
> str make_edge(param1=param1)

creates an edge

Used to set new edges. If the edge is formative, then a node is also formed. 

### Example 
```python
from __future__ import print_statement
import time
import pho_client
from pho_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pho_client.DefaultApi()
param1 = 'param1_example' # str | The value to update the key with. There can be 50 of those. For example;  param1=\"value1\", param2 =\"another value\" depending on the edge's default constructor variable count.  (optional)

try: 
    # creates an edge
    api_response = api_instance.make_edge(param1=param1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->make_edge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **param1** | **str**| The value to update the key with. There can be 50 of those. For example;  param1&#x3D;\&quot;value1\&quot;, param2 &#x3D;\&quot;another value\&quot; depending on the edge&#39;s default constructor variable count.  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_attribute**
> InlineResponse2004 set_attribute(value=value)

updates (or creates) an attribute

Works with all entities, including nodes and edges. Given its key, updates an  attribute value, or creates it, if it doesn't yet exist. 

### Example 
```python
from __future__ import print_statement
import time
import pho_client
from pho_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pho_client.DefaultApi()
value = 'value_example' # str | The value to update the key with. (optional)

try: 
    # updates (or creates) an attribute
    api_response = api_instance.set_attribute(value=value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->set_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| The value to update the key with. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

