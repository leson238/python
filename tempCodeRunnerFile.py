import logging
# import asyncio
# import json
# from urllib.request import urlopen
# import aiohttp
# import ssl
# # is the environment used to make request
# PROD_API_DOMAIN = 'http://api.something.cx/'
# API_SUFFIX = 'e/anything/'  # can be any string


# async def fetch(session, endpoint):
#     """Execute an http call async
#     Args:
#     session: contexte for making the http call
#     url: URL to call
#     Return:
#     responses: A dict like object containing http response
#     """
#     url = PROD_API_DOMAIN + API_SUFFIX + endpoint
#     async with session.get(url) as response:
#         resp = await response.text()
#     return resp


# async def on_request_start(
#         session, trace_config_ctx, params):
#     # print(trace_config_ctx)
#     print(params)
#     print("Starting request")


# async def on_request_end(session, trace_config_ctx, params):
#     print("Ending request")

# trace_config = aiohttp.TraceConfig()
# trace_config.on_request_start.append(on_request_start)
# trace_config.on_request_end.append(on_request_end)


# async def fetch_all(endpoints):
#     """ Gather many HTTP call made async
#     Args:
#     cities: a list of string
#     Return:
#     responses: A list of dict like object containing http response
#     """
#     bearer = "some_bearer_token_here"
#     headers = {'Authorization': 'Bearer ' + bearer,
#                }
#     connector = aiohttp.TCPConnector(ssl=False)
#     # print(dir(connector))
#     async with aiohttp.ClientSession(connector=connector, headers=headers, trace_configs=[trace_config]) as session:
#         tasks = []
#         for endpoint in endpoints:
#             tasks.append(
#                 fetch(
#                     session,
#                     endpoint
#                 )
#             )
#         responses = await asyncio.gather(*tasks, return_exceptions=True)
#     return responses


# def run_all_fetches(endpoints):
#     responses = asyncio.run(fetch_all(endpoints))
#     return responses


# logging.basicConfig(level=logging.DEBUG)
# test_urls = ["1", "2", "3", "4"]
# if __name__ == '__main__':
#     asyncio.run(run_all_fetches(test_urls))