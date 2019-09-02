#include <cstdio>
typedef long long int lld;

int main() {
    lld N, D;
    lld x, a, g, r;
    scanf_s("%lld %lld", &N, &D);
    for (lld i = 0; i < N; i++) {
        scanf_s("%lld %lld %lld %lld", &x, &a, &g, &r);
            if (x < a || (x - a) % (g + r) > g) {
                printf_s("NO");
                return 0;
            }
    }
    printf_s("YES");
    return 0;
}
