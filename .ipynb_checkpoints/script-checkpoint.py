import heapq

import heapq


def get_server_ids(num_servers, requests):
    # Initialize the heap with servers and their initial load (all 0)
    server_heap = [(0, i) for i in range(num_servers)]  # (load, server_id)
    heapq.heapify(server_heap)

    assigned_servers = []

    for request in requests:
        # Get the server with the least load (this will always be the root of the heap)
        load, server_id = heapq.heappop(server_heap)

        # Assign the request to this server
        assigned_servers.append(server_id)

        # After assigning the request, increase the load of this server
        heapq.heappush(server_heap, (load + 1, server_id))

    return assigned_servers


def test_get_server_ids():
    # Test Case 1: Basic Test with 3 servers and 5 requests
    num_servers = 3
    requests = [1, 2, 3, 4, 5]
    expected_output = [0, 1, 2, 0, 1]
    assert get_server_ids(num_servers, requests) == expected_output, "Test Case 1 Failed"

    # Test Case 2: One server handling all requests
    num_servers = 1
    requests = [1, 2, 3, 4, 5]
    expected_output = [0, 0, 0, 0, 0]  # All requests go to the single server (server 0)
    assert get_server_ids(num_servers, requests) == expected_output, "Test Case 2 Failed"

    # Test Case 3: Equal distribution of requests
    num_servers = 2
    requests = [1, 2, 3, 4, 5, 6]
    expected_output = [0, 1, 0, 1, 0, 1]  # Requests evenly split between two servers
    assert get_server_ids(num_servers, requests) == expected_output, "Test Case 3 Failed"

    # Test Case 4: Large number of servers, minimal requests
    num_servers = 10
    requests = [1, 2]
    expected_output = [0, 1]  # Requests assigned to server 0 and 1
    assert get_server_ids(num_servers, requests) == expected_output, "Test Case 4 Failed"

    # Test Case 5: Large number of requests, large number of servers
    num_servers = 5
    requests = list(range(1, 21))  # 20 requests
    expected_output = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
    assert get_server_ids(num_servers, requests) == expected_output, "Test Case 5 Failed"

    # Test Case 6: All servers have the same number of requests
    num_servers = 4
    requests = [1, 2, 3, 4, 5, 6, 7, 8]
    expected_output = [0, 1, 2, 3, 0, 1, 2, 3]  # Requests evenly distributed
    assert get_server_ids(num_servers, requests) == expected_output, "Test Case 6 Failed"

    num_servers = 5
    requests = [4,0,2,2]
    expected_output = [0, 0, 1, 2]  # Requests evenly distributed
    print(get_server_ids(num_servers,requests))
    assert get_server_ids(num_servers, requests) == expected_output, "Test Case 7 Failed"

    print("All test cases passed!")

# Run the tests
test_get_server_ids()

