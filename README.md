<div id="shields" align="center">

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Downloads][downloads-shield]][downloads-url]
[![GPLv3 License][license-shield]][license-url]
</div>

# cs2fade

Python port of [@chescos](https://github.com/chescos) original
[csgo-fade-percentage-calculator](https://github.com/chescos/csgo-fade-percentage-calculator).  
Check out his repository for more information.  
For a usage example, refer to [`example.py`](./example.py).

## Quick start

```python
import cs2fade

info = cs2fade.get("M4A1-S", 374)
print(f"#{info.ranking} / {info.percentage} / {info.finish}")
# => "#1 / 100.0 / fade"

info = cs2fade.get("M4A1-S", 739)
print(f"#{info.ranking} / {info.percentage} / {info.finish}")
# => "#1 / 80.0 / fade"
```

The helper infers the correct finish for the given weapon. If you need low-level
access to the calculators, the original classes remain available:

```python
from cs2fade import AcidFade

fade = AcidFade.get_percentage("SSG 08", 374)
```

If you notice any errors, please feel free to open an issue or pull request.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Helyux/cs2fade.svg?style=for-the-badge
[contributors-url]: https://github.com/Helyux/cs2fade/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Helyux/cs2fade.svg?style=for-the-badge
[forks-url]: https://github.com/Helyux/cs2fade/network/members
[stars-shield]: https://img.shields.io/github/stars/Helyux/cs2fade.svg?style=for-the-badge
[stars-url]: https://github.com/Helyux/cs2fade/stargazers
[issues-shield]: https://img.shields.io/github/issues/Helyux/cs2fade.svg?style=for-the-badge
[issues-url]: https://github.com/Helyux/cs2fade/issues
[downloads-shield]: https://img.shields.io/pepy/dt/cs2fade?style=for-the-badge
[downloads-url]: https://pepy.tech/project/cs2fade
[license-shield]: https://img.shields.io/badge/License-GPLv3-red.svg?style=for-the-badge
[license-url]: https://github.com/Helyux/cs2fade/blob/master/LICENSE
