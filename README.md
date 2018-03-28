# SimpleRandomString.py

## v0.01

Exactly what it says on the tin. This is a simple python script (barely even a script) that generates and prints a random ASCII string of the desired length. This length is currently specified by simply setting the value `n` in the actual code.

__WARNING__: Do not use this in any "real" application with serious crypto needs. "Don't roll your own crypto" as they say. There are plenty of libraries designed and vetted by actual crypto experts for use in important, complicated things. This is simply a little tool I use for my own convenience that I thought I'd share. Use at your own risk.

## Description and Usage

`SimpleRandomString.py` simply prints a random ASCII string of length `n`, where `n` is specified by the user by editing the code and replacing `n` in the `print` function (it's really just a big one-liner broken up for readability). This can obviously be quickly modified into a function that returns but does not print such a string, and I intend to include this feature in the future. The user may also choose, depending on their purpose, what *sorts* of ASCII characters they want to allow in generated strings by adding or removing `string.foo` terms from inside `.choice()`.

The core point of the tool is that it uses cryptographically secure system CSPRNGs. The regular `random` and things like `np.random` are not designed for cryptographically secure applications (in the case of the latter for example, the purpose is scientific/mathematical computing). `SimpleRandomString.py` uses the system CSPRNG via `random.SystemRandom()`, specifically:

* `CryptGenRandom()` on Windows, which you can read more about [here](https://msdn.microsoft.com/en-us/library/windows/desktop/aa379942(v=vs.85).aspx) and here.[1][2]
* `/dev/urandom/` on *nix-like systems. This is not intended to be an applied cryptography lesson, but if you want to know why `/dev/urandom/` is a better source of randomness in cryptographic scenarios than `/dev/random` on *nix, see [here](https://www.2uo.de/myths-about-urandom/). tl;dr, neither is "true randomness" (we are dealing with CS *P* RNGS) after all, the difference lies in blocking behavior.

[1]Yosifovich, P. et al. 2017. *Windows Internals 7th ed. Part 1*. Microsoft Press.

[2]Hart, J.M. 2010. *Windows System Programming 4th ed.* Addison-Wesley.