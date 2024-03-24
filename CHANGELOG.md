# CHANGELOG



## v0.3.0 (2024-03-24)

### Build

* build: configure pylance to ignore unused expressions

Using left and right shift operators to append nodes are highlighted by pylance as unused expressions, this new setting suppresses the warning. ([`725111e`](https://github.com/diasatta/bricka/commit/725111e6df25325d106ffe07e2a8c044026ee1c2))

### Documentation

* docs: update README.md ([`c210fae`](https://github.com/diasatta/bricka/commit/c210faedc6e92a2f2e22318859cc1199adcc234b))

### Feature

* feat: add support for styling

Bricka&#39;s components can now be directly styled from python, no need to write CSS manually.

The style API is inspired by StyleX.

Styles are authored as python typed dicts, with autocompletion for CSS property names.  Most of property values are constrained to a limited set of values, mimicking Tailwindcss constraints. Autocompletion is also supported for constrained values.

Bricka generates atomic CSS classes from the styles passed to html components, and supports automatic resolution of conflicting properties. Conflicting properties are inserted in different CSS layers so that the last applied style always wins.

Currently, Bricka supports pseudo-class selectors and media queries. ([`ba9dc18`](https://github.com/diasatta/bricka/commit/ba9dc180bdf90a3453ebd5cc77b3710c99773520))

### Fix

* fix: fix node&#39;s __enter__ method return type ([`5c38cc1`](https://github.com/diasatta/bricka/commit/5c38cc1878bb83e0ed1d7296420ae0fefeb90959))

* fix: fix constructor signature for container elements to accept int, float, str ([`64d0342`](https://github.com/diasatta/bricka/commit/64d0342f68b6813cf6c3e8b8d11803d6959a34d0))

### Test

* test: add tests for styling ([`9209e72`](https://github.com/diasatta/bricka/commit/9209e7204e300d438141262055d3f7b712ca3bbe))


## v0.2.0 (2024-03-19)

### Build

* build: add settings to type checker ([`ee2cac5`](https://github.com/diasatta/bricka/commit/ee2cac53e3ee5d8e5d79ef19ab65d72c71c00293))

* build: add a vscode task for testing ([`313625c`](https://github.com/diasatta/bricka/commit/313625c36a840272ec742b3e7f03c640e288aab3))

### Documentation

* docs: update README.md ([`8466103`](https://github.com/diasatta/bricka/commit/846610359b7edc5b71adc1e9c6ac91136acfa2e1))

### Feature

* feat: add all standard html elements and attributes

Standard HTML elements as well as standard attributes are supported. Deprecated elements and attributes are not supported. Experimental elements and attributes should be added progressively.

HTML elements include a MDN description as docstring, allowing to get a quick overview of the element on hover when using a proper IDE like VSCODE.

HTML attributes support autocompletion for attributes names as well as attribute values.

Attribute values are automatically escaped and URL attributes are URL-encoded. ([`4a0c734`](https://github.com/diasatta/bricka/commit/4a0c73496b36dbae264de655bd371dda512b7efb))

* feat: add support for multiply operator to clone nodes ([`700b728`](https://github.com/diasatta/bricka/commit/700b728cbe3618e8f833c14d7742ab904dc1173e))

* feat: add support for plus operator to create siblings ([`42f556a`](https://github.com/diasatta/bricka/commit/42f556a0c51ed0dc919211b199a821874519fb83))

* feat: add support for right and left shift operators ([`bd19c23`](https://github.com/diasatta/bricka/commit/bd19c233c47a1369a1d68899c408b26c3376f82d))

* feat: add support for node iterators ([`c6fde4a`](https://github.com/diasatta/bricka/commit/c6fde4ae7e8bd334b309c462617e49fb91296a08))

* feat: add support for node insertion by context managers ([`7a386a0`](https://github.com/diasatta/bricka/commit/7a386a0908e3c6b7e4ef0482f0c1a9fa291dd7df))

* feat: add node insertion methods ([`cafeb2e`](https://github.com/diasatta/bricka/commit/cafeb2ecbbb4630f44b3d99572dbe68f1e298991))

* feat: add core node classes ([`595ac18`](https://github.com/diasatta/bricka/commit/595ac1828826ddead85939fb037a3b9c2252617a))

### Test

* test: add tests for html elements and attributes ([`7e0f078`](https://github.com/diasatta/bricka/commit/7e0f07802b0f5a43ee439f5863d7322c571d1d7c))

* test: add tests for multiply operator ([`e2e37a5`](https://github.com/diasatta/bricka/commit/e2e37a5b361f3fd4560314a57fbe7d376313385f))

* test: add tests for plus operator ([`55029d4`](https://github.com/diasatta/bricka/commit/55029d4c6a7a087226ecc32fa2a914ccb6791c98))

* test: add tests for left and right shift operators ([`281c563`](https://github.com/diasatta/bricka/commit/281c56324d7e0a399294a90c6c99cbfc1db4d300))

* test: add tests for node iterator ([`b0b5041`](https://github.com/diasatta/bricka/commit/b0b5041c8c6c3eb7a7d0b01085a70eee023af9bc))

* test: add tests for context managers ([`bdcae32`](https://github.com/diasatta/bricka/commit/bdcae32b2417fe000e776582caf83db2d2e7c11b))

* test: add tests for node insertion ([`d7ffded`](https://github.com/diasatta/bricka/commit/d7ffded527c19ab43645f6917be7b566d57cf603))

* test: add tests for basic node rendering ([`224024e`](https://github.com/diasatta/bricka/commit/224024ee0a9e9f076bad7ffeb80c94a4068e1677))


## v0.1.12 (2024-03-17)

### Build

* build: fix ci-cd.yml ([`f20ad08`](https://github.com/diasatta/bricka/commit/f20ad08e6dee46f0559a522356602aafb6b147d5))

### Fix

* fix: fix tests ([`f9d0453`](https://github.com/diasatta/bricka/commit/f9d04533ccde20063553c209fa49d506c2fc97fb))


## v0.1.11 (2024-03-17)

### Fix

* fix: fix tests ([`1ac00c1`](https://github.com/diasatta/bricka/commit/1ac00c1129c0c6cf4dcec4362e77b1f057e1f2a1))


## v0.1.10 (2024-03-17)

### Fix

* fix: fix pyproject.toml ([`b1ba1d9`](https://github.com/diasatta/bricka/commit/b1ba1d9b05ecf2540df0d7ff9b26bfef7edda9ad))

* fix: fix pyproject.toml ([`6b57155`](https://github.com/diasatta/bricka/commit/6b57155696755e16b18b82026c24e8c82094daef))

### Unknown

* Merge branch &#39;develop&#39; ([`1f98586`](https://github.com/diasatta/bricka/commit/1f9858663b5e37c7fcf2e7942a3fee1e9b14ce11))


## v0.1.9 (2024-03-17)

### Fix

* fix: fix tests ([`e8f0350`](https://github.com/diasatta/bricka/commit/e8f0350f0c432dd3a58c530f0733d971774567db))

* fix: fix tests ([`04bd656`](https://github.com/diasatta/bricka/commit/04bd6565c711a950bfa63f65a468bc211405a954))

### Unknown

* Merge branch &#39;develop&#39; ([`71eb0a7`](https://github.com/diasatta/bricka/commit/71eb0a71d75e1b0054ae96078e87804111a56218))


## v0.1.8 (2024-03-17)

### Unknown

* Merge branch &#39;develop&#39; ([`86ed491`](https://github.com/diasatta/bricka/commit/86ed49103e242c0c72c4ad84dad0637dfd79e2ce))


## v0.1.7 (2024-03-17)

### Fix

* fix: fix ci-cd.yml ([`d42d51d`](https://github.com/diasatta/bricka/commit/d42d51d2f13d731d29788f8d895597fc264505e7))

* fix: fix ci-cd.yml ([`c66f83e`](https://github.com/diasatta/bricka/commit/c66f83ea32bd192d86ab4d4702476ab7528e2e28))


## v0.1.6 (2024-03-17)

### Fix

* fix: fix tests to check CI/CD ([`c6b50d6`](https://github.com/diasatta/bricka/commit/c6b50d6ab5d4d53a5baf77cadebb6eaa71e300c0))

* fix: fix tests to check CI/CD ([`6040d8e`](https://github.com/diasatta/bricka/commit/6040d8e1a14a4f50520765713a3e90dc11e69d8d))

### Unknown

* Merge branch &#39;develop&#39; ([`173efab`](https://github.com/diasatta/bricka/commit/173efab9f3b950296f5d17e14b91095af973b055))


## v0.1.5 (2024-03-17)

### Build

* build: update tests ([`959ac5c`](https://github.com/diasatta/bricka/commit/959ac5c682f28bbc08a4978cb7f0a4feb09ecc1b))

### Fix

* fix: fix ci-cd.yml to automatically build package ([`1546ec5`](https://github.com/diasatta/bricka/commit/1546ec5ef7326d064069d8ce73ba9ee7862248ee))

### Unknown

* Merge branch &#39;develop&#39; ([`cdffc04`](https://github.com/diasatta/bricka/commit/cdffc04a873938a035917d771ced6b78072e103b))


## v0.1.4 (2024-03-17)

### Build

* build: update semantic-release config ([`56dfbb5`](https://github.com/diasatta/bricka/commit/56dfbb5df5cb60b9edd5ce5679d48389523377ea))

* build: add semantic-release as a dev dependency ([`dfef517`](https://github.com/diasatta/bricka/commit/dfef51796333ce4ac96e40057030b7fa5f64277c))

### Fix

* fix: fix tests to check CI/CD ([`e827fc5`](https://github.com/diasatta/bricka/commit/e827fc5c0349e4bf3d5a422dce801a642b9ce33e))


## v0.1.3 (2024-03-17)

### Build

* build: bump version number ([`ac65adc`](https://github.com/diasatta/bricka/commit/ac65adc9e4dd33e392c61660ce15781da7158b4b))

* build: update ci-cd.yml ([`4d34c10`](https://github.com/diasatta/bricka/commit/4d34c1054fa7fde67e5f66deca4caf61e6ed3689))


## v0.1.2 (2024-03-17)

### Build

* build: bump version number ([`2efbfa0`](https://github.com/diasatta/bricka/commit/2efbfa02dd55ae846f54dc4ae7a0da0b6ad47719))

* build: update tests to check CI/CD 2 ([`5faf1fb`](https://github.com/diasatta/bricka/commit/5faf1fb9dff3d7fb4bfbb108a90588a2a05dee3a))


## v0.1.1 (2024-03-17)

### Build

* build: bump version number ([`98959fe`](https://github.com/diasatta/bricka/commit/98959fe656e87432da5e31d3c60d82feb3a2d5c0))

* build: update tests to check CI/CD ([`96da7ec`](https://github.com/diasatta/bricka/commit/96da7ec7718f52561f727fa39129809dd43d44b7))

* build: add cd to workflow ([`f3d7c50`](https://github.com/diasatta/bricka/commit/f3d7c50b86f0656f41cae5fae5c20478dd281b5f))

* build: update files to test CI/CD ([`4e84a78`](https://github.com/diasatta/bricka/commit/4e84a7838a14189ca58ba2d80d83bbf651b79a89))

* build: add cd to workflow ([`a75ac56`](https://github.com/diasatta/bricka/commit/a75ac56aef76d5d23de3f1e691b62b19198c9f0c))

* build: update files to test CI/CD ([`fb7965e`](https://github.com/diasatta/bricka/commit/fb7965e359fa3776eb891ace9e510d9e4b0a4a28))

* build: update tests to test branching model ([`0e72860`](https://github.com/diasatta/bricka/commit/0e72860f2536bd112a5e3fac5e398ba3b48849a3))

* build: add pytest-cov as a dev dependency ([`67651a9`](https://github.com/diasatta/bricka/commit/67651a9ec76984b0bdbf79f70fea073962ba8ea3))

* build: add pytest as a dev dependency ([`6cfe6e7`](https://github.com/diasatta/bricka/commit/6cfe6e73f63a01db10382779bd2e3e803029bc89))

* build: update poetry lock ([`3b13fe1`](https://github.com/diasatta/bricka/commit/3b13fe19b6cfe138171b0670178aa9c272e279a2))

* build: project setup ([`d94ad85`](https://github.com/diasatta/bricka/commit/d94ad8583465c79f78e6be68fb9a2f1f6e1d0416))

### Feature

* feat: create initial node class ([`9ba78bf`](https://github.com/diasatta/bricka/commit/9ba78bfbed8592b349fa0a318a00ea51caa8fc6d))

### Test

* test: fix sample test ([`3e9e996`](https://github.com/diasatta/bricka/commit/3e9e996353d892c5d6ed9fd4a112642ab370a390))

* test: update sample tests ([`61ed49a`](https://github.com/diasatta/bricka/commit/61ed49a186b790c5e59cff434782ab3e6ae70841))

* test: add sample test ([`93999ca`](https://github.com/diasatta/bricka/commit/93999ca94f96eda386d8b3109f217f89a503e690))

### Unknown

* Merge branch &#39;develop&#39; ([`134edac`](https://github.com/diasatta/bricka/commit/134edac282c3feaba1a4e47bc879af37a66c9641))

* Merge pull request #1 from diasatta/develop

build: update tests to test branching model ([`8564489`](https://github.com/diasatta/bricka/commit/8564489d2ae4871ddddd2c9d96fe9c30523d9e19))

* Update ci-cd.yml ([`ccc2a53`](https://github.com/diasatta/bricka/commit/ccc2a5357ac760644aaa50a7092e7b6971c632a6))

* Rename blank.yml to ci-cd.yml ([`9187991`](https://github.com/diasatta/bricka/commit/9187991e861469335e5b2fc771bd0162c3bf96c7))

* Create blank.yml ([`7fd48ad`](https://github.com/diasatta/bricka/commit/7fd48ad805134f03183f761adf44884a0cedec68))


## v0.1.0 (2024-03-13)

### Documentation

* docs: update README.md ([`b8ae735`](https://github.com/diasatta/bricka/commit/b8ae7356e4379b0969ad6f89dc101d0688d0fb9d))

### Unknown

* Initial commit ([`6987534`](https://github.com/diasatta/bricka/commit/6987534206c98aef40771810c40d9385bf9079ab))
