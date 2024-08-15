// # evdschat - An open-source Python package for enhanced data retrieval.
// # Copyright (c) 2024 Sermet Pekin
// # Licensed under the Creative Commons Attribution-NonCommercial 4.0 International License.
// # You may not use this file except in compliance with the License.
// # You may obtain a copy of the License at
// #
// #     https://creativecommons.org/licenses/by-nc/4.0/
// #
// # Unless required by applicable law or agreed to in writing, software
// # distributed under the License is distributed on an "AS IS" BASIS,
// # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// # See the License for the specific language governing permissions and
// # limitations under the License.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <curl/curl.h>
typedef struct
{
    char *memory;
    size_t size;
} response_data;

typedef struct
{
    const char *url;
    const char *prompt;
    const char *api_key;
    const char *proxy_url;
} post_params;

static size_t WriteCallback(void *contents, size_t size, size_t nmemb, void *userp)
{
    size_t realsize = size * nmemb;
    response_data *mem = (response_data *)userp;

    char *ptr = (char *)realloc(mem->memory, mem->size + realsize + 1);
    if (ptr == NULL)
        return 0; // Realloc failed

    mem->memory = ptr;
    memcpy(&(mem->memory[mem->size]), contents, realsize);
    mem->size += realsize;
    mem->memory[mem->size] = 0;

    return realsize;
}

const char *get_proxy_for_url(const char *url, const char *proxy_url)
{
    if (proxy_url != NULL)
        return proxy_url;

    const char *https_proxy = getenv("HTTPS_PROXY");
    const char *http_proxy = getenv("HTTP_PROXY");

    if (strncmp(url, "https", 5) == 0 && https_proxy != NULL)
    {
        return https_proxy;
    }
    else if (http_proxy != NULL)
    {
        return http_proxy;
    }
    return NULL;
}

char *post_request(const post_params *params)
{

    CURL *curl;
    CURLcode res;
    response_data chunk;

    chunk.memory = malloc(1);
    if (chunk.memory == NULL)
    {
        fprintf(stderr, "Failed to allocate memory.\n");
        return NULL;
    }
    chunk.memory[0] = 0;
    chunk.size = 0;

    if (curl_global_init(CURL_GLOBAL_DEFAULT) != 0)
    {
        fprintf(stderr, "Failed to initialize curl.\n");
        free(chunk.memory);
        return NULL;
    }

    curl = curl_easy_init();
    if (curl)
    {
        char data[1024];
        snprintf(data, sizeof(data), "{\"prompt\": \"%s\", \"api_key\": \"%s\"}", params->prompt, params->api_key);

        curl_easy_setopt(curl, CURLOPT_URL, params->url);
        curl_easy_setopt(curl, CURLOPT_POST, 1L);
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, data);

        struct curl_slist *headers = NULL;
        headers = curl_slist_append(headers, "Content-Type: application/json");
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);

        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, (void *)&chunk);

        const char *proxy_url_env = get_proxy_for_url(params->url, params->proxy_url);
        if (proxy_url_env != NULL)
        {
            curl_easy_setopt(curl, CURLOPT_PROXY, proxy_url_env);
        }

        res = curl_easy_perform(curl);

        if (res != CURLE_OK)
        {
            fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
            free(chunk.memory);
            chunk.memory = NULL;
        }

        curl_easy_cleanup(curl);
        curl_slist_free_all(headers);
    }
    else
    {
        fprintf(stderr, "curl_easy_init() failed.\n");
        free(chunk.memory);
        chunk.memory = NULL;
    }

    curl_global_cleanup();

    return chunk.memory;
}

void free_memory(char *ptr)
{
    if (ptr)
    {
        free(ptr);
    }
}

// gcc -shared -o libpost_request.so -fPIC ./evdschat/src/getter.c -lcurl
