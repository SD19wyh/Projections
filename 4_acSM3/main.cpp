#include <string.h>
#include <stdio.h>
#include <iostream>
#include <windows.h>
#include "sm3.h"

int main(int argc, char* argv[])
{
    DWORD star_time = GetTickCount();
    auto* input = (unsigned char*)"abc";   // input
    int ilen = 3;                   // input length
    unsigned char output[32];       // output
    int i;
    sm3_context ctx;                // struct

    printf("Message:\n");
    for (i = 0; i < 16; i++)
        printf("abcd");
    printf("\n");

    sm3_starts(&ctx);
    for (i = 0; i < 16; i++)
        sm3_update(&ctx, (unsigned char*)"abcd", 4);
    sm3_finish(&ctx, output);
    memset(&ctx, 0, sizeof(sm3_context));

    printf("Hash:\n");
    for (i = 0; i < 32; i++)
    {
        printf("%02x", output[i]);
        if (((i + 1) % 4) == 0) printf(" ");
    }
    printf("\n");
    DWORD end_time = GetTickCount();
    std::cout << "The total time is:" << (end_time - star_time) << "ms." << std::endl;
}