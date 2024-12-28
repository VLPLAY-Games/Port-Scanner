#include <string>

#ifdef _WIN32
#include <winsock2.h>
#include <ws2tcpip.h>
#pragma comment(lib, "Ws2_32.lib")
#else
#include <arpa/inet.h>
#include <netdb.h>
#include <unistd.h>
#endif

using namespace std;

extern "C" __declspec(dllexport) const char* get_device_name(const char* ip) {
    static string result;

#ifdef _WIN32
    // Windows: используем Windows API
    WSADATA wsaData;
    WSAStartup(MAKEWORD(2, 2), &wsaData);

    struct addrinfo hints = { 0 }, * res;
    hints.ai_family = AF_INET;

    if (getaddrinfo(ip, NULL, &hints, &res) != 0) {
        return nullptr;  // Имя устройства не найдено
    }

    char host[NI_MAXHOST];
    if (getnameinfo(res->ai_addr, res->ai_addrlen, host, sizeof(host), NULL, 0, 0) != 0) {
        freeaddrinfo(res);
        WSACleanup();
        return nullptr;
    }

    result = string(host);
    freeaddrinfo(res);
    WSACleanup();
#else
    // Linux: используем стандартные POSIX функции
    struct sockaddr_in sa;
    char host[1024];

    sa.sin_family = AF_INET;
    sa.sin_addr.s_addr = inet_addr(ip);

    if (getnameinfo((struct sockaddr*)&sa, sizeof(sa), host, sizeof(host), NULL, 0, 0) != 0) {
        return nullptr;  // Имя устройства не найдено
    }

    result = string(host);
#endif

    return result.c_str();
}
