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


struct response_data {
    char *memory;
    size_t size;
};


static size_t WriteCallback(void *contents, size_t size, size_t nmemb, void *userp) {
    size_t realsize = size * nmemb;
    struct response_data *mem = (struct response_data *)userp;

    char *ptr =(char * ) realloc(mem->memory, mem->size + realsize + 1);
    if(ptr == NULL) return 0;  

    mem->memory = ptr;
    memcpy(&(mem->memory[mem->size]), contents, realsize);
    mem->size += realsize;
    mem->memory[mem->size] = 0;

    return realsize;
}

char* post_request(const char *url, const char *prompt, const char *api_key) {
    CURL *curl;
    CURLcode res;
    struct response_data chunk;

    chunk.memory = malloc(1);  // Initial memory allocation
    chunk.size = 0;            // No data at this point

    curl_global_init(CURL_GLOBAL_DEFAULT);
    curl = curl_easy_init();

    if(curl) {
        // Prepare the JSON payload
        char data[1024];
        snprintf(data, sizeof(data), "{\"prompt\": \"%s\", \"api_key\": \"%s\"}", prompt, api_key);

        curl_easy_setopt(curl, CURLOPT_URL, url);
        curl_easy_setopt(curl, CURLOPT_POST, 1L);
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, data);
        
        struct curl_slist *headers = NULL;
        headers = curl_slist_append(headers, "Content-Type: application/json");
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);

        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, (void *)&chunk);

        res = curl_easy_perform(curl);

        if(res != CURLE_OK) {
            fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
        }

        curl_easy_cleanup(curl);
        curl_slist_free_all(headers);
    }

    curl_global_cleanup();

    return chunk.memory;
}

void free_memory(char *ptr) {
    if (ptr) {
        free(ptr);
    }
}
// gcc -shared -o libpost_request.so -fPIC ./evdschat/src/getter.c -lcurl
