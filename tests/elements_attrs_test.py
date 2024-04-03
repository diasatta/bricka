from bricka.elements import *
from bricka.node import Element

class TestElementAttrs():
  def test_accesskey(self) -> None:
    assert Element(accesskey="foo").render_attrs() == 'accesskey="foo"'

  def test_autocapitalize(self) -> None:
    assert Element(autocapitalize="foo").render_attrs() == 'autocapitalize="foo"'

  def test_autofocus(self) -> None:
    assert Element(autofocus=True).render_attrs() == 'autofocus'

  def test_class_(self) -> None:
    assert Element(class_="foo").render_attrs() == 'class="foo"'

  def test_contenteditable(self) -> None:
    assert Element(contenteditable="foo").render_attrs() == 'contenteditable="foo"'

  def test_dir(self) -> None:
    assert Element(dir="auto").render_attrs() == 'dir="auto"'

  def test_draggable(self) -> None:
    assert Element(draggable="false").render_attrs() == 'draggable="false"'

  def test_enterkeyhint(self) -> None:
    assert Element(enterkeyhint="foo").render_attrs() == 'enterkeyhint="foo"'

  def test_hidden(self) -> None:
    assert Element(hidden="true").render_attrs() == 'hidden="true"'

  def test_id(self) -> None:
    assert Element(id="foo").render_attrs() == 'id="foo"'

  def test_inert(self) -> None:
    assert Element(inert=True).render_attrs() == 'inert'

  def test_inputmode(self) -> None:
    assert Element(inputmode="email").render_attrs() == 'inputmode="email"'

  def test_is_(self) -> None:
    assert Element(is_="foo").render_attrs() == 'is="foo"'

  def test_itemid(self) -> None:
    assert Element(itemid="foo").render_attrs() == 'itemid="foo"'

  def test_itemprop(self) -> None:
    assert Element(itemprop="foo").render_attrs() == 'itemprop="foo"'

  def test_itemref(self) -> None:
    assert Element(itemref="foo").render_attrs() == 'itemref="foo"'

  def test_itemscope(self) -> None:
    assert Element(itemscope=True).render_attrs() == 'itemscope'

  def test_itemtype(self) -> None:
    assert Element(itemtype='www.foo.bar/baz/?quux="1"').render_attrs() == 'itemtype="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_lang(self) -> None:
    assert Element(lang="foo").render_attrs() == 'lang="foo"'

  def test_nonce(self) -> None:
    assert Element(nonce="foo").render_attrs() == 'nonce="foo"'

  def test_part(self) -> None:
    assert Element(part="foo").render_attrs() == 'part="foo"'

  def test_popover(self) -> None:
    assert Element(popover="foo").render_attrs() == 'popover="foo"'

  def test_role(self) -> None:
    assert Element(role="alert").render_attrs() == 'role="alert"'

  def test_slot(self) -> None:
    assert Element(slot="foo").render_attrs() == 'slot="foo"'

  def test_spellcheck(self) -> None:
    assert Element(spellcheck="false").render_attrs() == 'spellcheck="false"'

  def test_style(self) -> None:
    assert Element(style="width: 1px;").render_attrs() == 'style="width: 1px;"'

  def test_tabindex(self) -> None:
    assert Element(tabindex="foo").render_attrs() == 'tabindex="foo"'

  def test_title(self) -> None:
    assert Element(title="foo").render_attrs() == 'title="foo"'

  def test_translate(self) -> None:
    assert Element(translate="no").render_attrs() == 'translate="no"'

  def test_virtualkeyboardpolicy(self) -> None:
    assert Element(virtualkeyboardpolicy="foo").render_attrs() == 'virtualkeyboardpolicy="foo"'

class TestAAttrs():
  def test_download(self) -> None:
    assert A(download="foo").render_attrs() == 'download="foo"'

  def test_href(self) -> None:
    assert A(href='www.foo.bar/baz/?quux="1"').render_attrs() == 'href="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_hreflang(self) -> None:
    assert A(hreflang="foo").render_attrs() == 'hreflang="foo"'

  def test_ping(self) -> None:
    assert A(ping='www.foo.bar/baz/?quux="1"').render_attrs() == 'ping="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_referrerpolicy(self) -> None:
    assert A(referrerpolicy="no-referrer").render_attrs() == 'referrerpolicy="no-referrer"'

  def test_rel(self) -> None:
    assert A(rel="alternate").render_attrs() == 'rel="alternate"'

  def test_target(self) -> None:
    assert A(target="_blank").render_attrs() == 'target="_blank"'

  def test_type(self) -> None:
    assert A(type="foo").render_attrs() == 'type="foo"'

class TestAreaAttrs():
  def test_alt(self) -> None:
    assert Area(alt="foo").render_attrs() == 'alt="foo"'

  def test_coords(self) -> None:
    assert Area(coords="foo").render_attrs() == 'coords="foo"'

  def test_download(self) -> None:
    assert Area(download="foo").render_attrs() == 'download="foo"'

  def test_href(self) -> None:
    assert Area(href='www.foo.bar/baz/?quux="1"').render_attrs() == 'href="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_ping(self) -> None:
    assert Area(ping='www.foo.bar/baz/?quux="1"').render_attrs() == 'ping="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_referrerpolicy(self) -> None:
    assert Area(referrerpolicy="no-referrer").render_attrs() == 'referrerpolicy="no-referrer"'

  def test_rel(self) -> None:
    assert Area(rel="alternate").render_attrs() == 'rel="alternate"'

  def test_shape(self) -> None:
    assert Area(shape="circle").render_attrs() == 'shape="circle"'

  def test_target(self) -> None:
    assert Area(target="_blank").render_attrs() == 'target="_blank"'

class TestAudioAttrs():
  def test_autoplay(self) -> None:
    assert Audio(autoplay=True).render_attrs() == 'autoplay'

  def test_controls(self) -> None:
    assert Audio(controls=True).render_attrs() == 'controls'

  def test_crossorigin(self) -> None:
    assert Audio(crossorigin="anonymous").render_attrs() == 'crossorigin="anonymous"'

  def test_loop(self) -> None:
    assert Audio(loop=True).render_attrs() == 'loop'

  def test_muted(self) -> None:
    assert Audio(muted=True).render_attrs() == 'muted'

  def test_preload(self) -> None:
    assert Audio(preload="auto").render_attrs() == 'preload="auto"'

  def test_src(self) -> None:
    assert Audio(src='www.foo.bar/baz/?quux="1"').render_attrs() == 'src="www.foo.bar/baz/?quux=&quot;1&quot;"'

class TestBaseAttrs():
  def test_href(self) -> None:
    assert Base(href='www.foo.bar/baz/?quux="1"').render_attrs() == 'href="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_target(self) -> None:
    assert Base(target="_blank").render_attrs() == 'target="_blank"'

class TestBlockquoteAttrs():
  def test_cite(self) -> None:
    assert Blockquote(cite='www.foo.bar/baz/?quux="1"').render_attrs() == 'cite="www.foo.bar/baz/?quux=&quot;1&quot;"'

class TestBodyAttrs():
  def test_onafterprint(self) -> None:
    assert Body(onafterprint="foo()").render_attrs() == 'onafterprint="foo()"'

  def test_onbeforeprint(self) -> None:
    assert Body(onbeforeprint="foo()").render_attrs() == 'onbeforeprint="foo()"'

  def test_onbeforeunload(self) -> None:
    assert Body(onbeforeunload="foo()").render_attrs() == 'onbeforeunload="foo()"'

  def test_onblur(self) -> None:
    assert Body(onblur="foo()").render_attrs() == 'onblur="foo()"'

  def test_onerror(self) -> None:
    assert Body(onerror="foo()").render_attrs() == 'onerror="foo()"'

  def test_onfocus(self) -> None:
    assert Body(onfocus="foo()").render_attrs() == 'onfocus="foo()"'

  def test_onhashchange(self) -> None:
    assert Body(onhashchange="foo()").render_attrs() == 'onhashchange="foo()"'

  def test_onlanguagechange(self) -> None:
    assert Body(onlanguagechange="foo()").render_attrs() == 'onlanguagechange="foo()"'

  def test_onload(self) -> None:
    assert Body(onload="foo()").render_attrs() == 'onload="foo()"'

  def test_onmessage(self) -> None:
    assert Body(onmessage="foo()").render_attrs() == 'onmessage="foo()"'

  def test_onoffline(self) -> None:
    assert Body(onoffline="foo()").render_attrs() == 'onoffline="foo()"'

  def test_ononline(self) -> None:
    assert Body(ononline="foo()").render_attrs() == 'ononline="foo()"'

  def test_onpopstate(self) -> None:
    assert Body(onpopstate="foo()").render_attrs() == 'onpopstate="foo()"'

  def test_onredo(self) -> None:
    assert Body(onredo="foo()").render_attrs() == 'onredo="foo()"'

  def test_onresize(self) -> None:
    assert Body(onresize="foo()").render_attrs() == 'onresize="foo()"'

  def test_onstorage(self) -> None:
    assert Body(onstorage="foo()").render_attrs() == 'onstorage="foo()"'

  def test_onundo(self) -> None:
    assert Body(onundo="foo()").render_attrs() == 'onundo="foo()"'

  def test_onunload(self) -> None:
    assert Body(onunload="foo()").render_attrs() == 'onunload="foo()"'

class TestButtonAttrs():
  def test_autofocus(self) -> None:
    assert Button(autofocus=True).render_attrs() == 'autofocus'

  def test_disabled(self) -> None:
    assert Button(disabled=True).render_attrs() == 'disabled'

  def test_form(self) -> None:
    assert Button(form="foo").render_attrs() == 'form="foo"'

  def test_formaction(self) -> None:
    assert Button(formaction='www.foo.bar/baz/?quux="1"').render_attrs() == 'formaction="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_formenctype(self) -> None:
    assert Button(formenctype="application/x-www-form-urlencoded").render_attrs() == 'formenctype="application/x-www-form-urlencoded"'

  def test_formmethod(self) -> None:
    assert Button(formmethod="get").render_attrs() == 'formmethod="get"'

  def test_formnovalidate(self) -> None:
    assert Button(formnovalidate=True).render_attrs() == 'formnovalidate'

  def test_formtarget(self) -> None:
    assert Button(formtarget="_blank").render_attrs() == 'formtarget="_blank"'

  def test_name(self) -> None:
    assert Button(name="foo").render_attrs() == 'name="foo"'

  def test_type(self) -> None:
    assert Button(type="button").render_attrs() == 'type="button"'

  def test_value(self) -> None:
    assert Button(value="foo").render_attrs() == 'value="foo"'

class TestCanvasAttrs():
  def test_height(self) -> None:
    assert Canvas(height="foo").render_attrs() == 'height="foo"'

  def test_width(self) -> None:
    assert Canvas(width="foo").render_attrs() == 'width="foo"'

class TestColAttrs():
  def test_span(self) -> None:
    assert Col(span="foo").render_attrs() == 'span="foo"'

class TestColgroupAttrs():
  def test_span(self) -> None:
    assert Colgroup(span="foo").render_attrs() == 'span="foo"'

class TestDataAttrs():
  def test_value(self) -> None:
    assert Data(value="foo").render_attrs() == 'value="foo"'

class TestDelAttrs():
  def test_cite(self) -> None:
    assert Del(cite='www.foo.bar/baz/?quux="1"').render_attrs() == 'cite="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_datetime(self) -> None:
    assert Del(datetime="foo").render_attrs() == 'datetime="foo"'

class TestDetailsAttrs():
  def test_open(self) -> None:
    assert Details(open=True).render_attrs() == 'open'

class TestDialogAttrs():
  def test_open(self) -> None:
    assert Dialog(open=True).render_attrs() == 'open'

class TestEmbedAttrs():
  def test_height(self) -> None:
    assert Embed(height="foo").render_attrs() == 'height="foo"'

  def test_src(self) -> None:
    assert Embed(src='www.foo.bar/baz/?quux="1"').render_attrs() == 'src="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_type(self) -> None:
    assert Embed(type="foo").render_attrs() == 'type="foo"'

  def test_width(self) -> None:
    assert Embed(width="foo").render_attrs() == 'width="foo"'

class TestFieldsetAttrs():
  def test_disabled(self) -> None:
    assert Fieldset(disabled=True).render_attrs() == 'disabled'

  def test_form(self) -> None:
    assert Fieldset(form="foo").render_attrs() == 'form="foo"'

  def test_name(self) -> None:
    assert Fieldset(name="foo").render_attrs() == 'name="foo"'

class TestFormAttrs():
  def test_accept_charset(self) -> None:
    assert Form(accept_charset="foo").render_attrs() == 'accept-charset="foo"'

  def test_action(self) -> None:
    assert Form(action='www.foo.bar/baz/?quux="1"').render_attrs() == 'action="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_autocomplete(self) -> None:
    assert Form(autocomplete="additional-name").render_attrs() == 'autocomplete="additional-name"'

  def test_enctype(self) -> None:
    assert Form(enctype="application/x-www-form-urlencoded").render_attrs() == 'enctype="application/x-www-form-urlencoded"'

  def test_method(self) -> None:
    assert Form(method="get").render_attrs() == 'method="get"'

  def test_name(self) -> None:
    assert Form(name="foo").render_attrs() == 'name="foo"'

  def test_novalidate(self) -> None:
    assert Form(novalidate=True).render_attrs() == 'novalidate'

  def test_rel(self) -> None:
    assert Form(rel="alternate").render_attrs() == 'rel="alternate"'

  def test_target(self) -> None:
    assert Form(target="_blank").render_attrs() == 'target="_blank"'

class TestHtmlAttrs():
  def test_xmlns(self) -> None:
    assert Html(xmlns='www.foo.bar/baz/?quux="1"').render_attrs() == 'xmlns="www.foo.bar/baz/?quux=&quot;1&quot;"'  # type: ignore

class TestIframeAttrs():
  def test_allow(self) -> None:
    assert Iframe(allow="foo").render_attrs() == 'allow="foo"'

  def test_allowfullscreen(self) -> None:
    assert Iframe(allowfullscreen="false").render_attrs() == 'allowfullscreen="false"'

  def test_height(self) -> None:
    assert Iframe(height="foo").render_attrs() == 'height="foo"'

  def test_loading(self) -> None:
    assert Iframe(loading="eager").render_attrs() == 'loading="eager"'

  def test_name(self) -> None:
    assert Iframe(name="foo").render_attrs() == 'name="foo"'

  def test_referrerpolicy(self) -> None:
    assert Iframe(referrerpolicy="no-referrer").render_attrs() == 'referrerpolicy="no-referrer"'

  def test_sandbox(self) -> None:
    assert Iframe(sandbox="allow-forms").render_attrs() == 'sandbox="allow-forms"'

  def test_src(self) -> None:
    assert Iframe(src='www.foo.bar/baz/?quux="1"').render_attrs() == 'src="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_srcdoc(self) -> None:
    assert Iframe(srcdoc='<foo class="bar"></foo>').render_attrs() == 'srcdoc="&lt;foo class=&quot;bar&quot;&gt;&lt;/foo&gt;"'

  def test_width(self) -> None:
    assert Iframe(width="foo").render_attrs() == 'width="foo"'

class TestImgAttrs():
  def test_alt(self) -> None:
    assert Img(alt="foo").render_attrs() == 'alt="foo"'

  def test_crossorigin(self) -> None:
    assert Img(crossorigin="anonymous").render_attrs() == 'crossorigin="anonymous"'

  def test_decoding(self) -> None:
    assert Img(decoding="async").render_attrs() == 'decoding="async"'

  def test_fetchpriority(self) -> None:
    assert Img(fetchpriority="auto").render_attrs() == 'fetchpriority="auto"'

  def test_height(self) -> None:
    assert Img(height="foo").render_attrs() == 'height="foo"'

  def test_ismap(self) -> None:
    assert Img(ismap=True).render_attrs() == 'ismap'

  def test_loading(self) -> None:
    assert Img(loading="eager").render_attrs() == 'loading="eager"'

  def test_referrerpolicy(self) -> None:
    assert Img(referrerpolicy="no-referrer").render_attrs() == 'referrerpolicy="no-referrer"'

  def test_sizes(self) -> None:
    assert Img(sizes="foo").render_attrs() == 'sizes="foo"'

  def test_src(self) -> None:
    assert Img(src='www.foo.bar/baz/?quux="1"').render_attrs() == 'src="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_srcset(self) -> None:
    assert Img(srcset='www.foo.bar/baz/?quux="1"').render_attrs() == 'srcset="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_usemap(self) -> None:
    assert Img(usemap='www.foo.bar/baz/?quux="1"').render_attrs() == 'usemap="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_width(self) -> None:
    assert Img(width="foo").render_attrs() == 'width="foo"'

class TestInputAttrs():
  def test_accept(self) -> None:
    assert Input(accept="audio/*").render_attrs() == 'accept="audio/*"'

  def test_alt(self) -> None:
    assert Input(alt="foo").render_attrs() == 'alt="foo"'

  def test_autocomplete(self) -> None:
    assert Input(autocomplete="additional-name").render_attrs() == 'autocomplete="additional-name"'

  def test_autofocus(self) -> None:
    assert Input(autofocus=True).render_attrs() == 'autofocus'

  def test_capture(self) -> None:
    assert Input(capture="foo").render_attrs() == 'capture="foo"'

  def test_checked(self) -> None:
    assert Input(checked=True).render_attrs() == 'checked'

  def test_dirname(self) -> None:
    assert Input(dirname="foo").render_attrs() == 'dirname="foo"'

  def test_disabled(self) -> None:
    assert Input(disabled=True).render_attrs() == 'disabled'

  def test_form(self) -> None:
    assert Input(form="foo").render_attrs() == 'form="foo"'

  def test_formaction(self) -> None:
    assert Input(formaction='www.foo.bar/baz/?quux="1"').render_attrs() == 'formaction="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_formenctype(self) -> None:
    assert Input(formenctype="application/x-www-form-urlencoded").render_attrs() == 'formenctype="application/x-www-form-urlencoded"'

  def test_formmethod(self) -> None:
    assert Input(formmethod="get").render_attrs() == 'formmethod="get"'

  def test_formnovalidate(self) -> None:
    assert Input(formnovalidate=True).render_attrs() == 'formnovalidate'

  def test_formtarget(self) -> None:
    assert Input(formtarget="_blank").render_attrs() == 'formtarget="_blank"'

  def test_height(self) -> None:
    assert Input(height="foo").render_attrs() == 'height="foo"'

  def test_list(self) -> None:
    assert Input(list="foo").render_attrs() == 'list="foo"'

  def test_max(self) -> None:
    assert Input(max="foo").render_attrs() == 'max="foo"'

  def test_maxlength(self) -> None:
    assert Input(maxlength="foo").render_attrs() == 'maxlength="foo"'

  def test_min(self) -> None:
    assert Input(min="foo").render_attrs() == 'min="foo"'

  def test_minlength(self) -> None:
    assert Input(minlength="foo").render_attrs() == 'minlength="foo"'

  def test_multiple(self) -> None:
    assert Input(multiple=True).render_attrs() == 'multiple'

  def test_name(self) -> None:
    assert Input(name="foo").render_attrs() == 'name="foo"'

  def test_pattern(self) -> None:
    assert Input(pattern="foo").render_attrs() == 'pattern="foo"'

  def test_placeholder(self) -> None:
    assert Input(placeholder="foo").render_attrs() == 'placeholder="foo"'

  def test_readonly(self) -> None:
    assert Input(readonly=True).render_attrs() == 'readonly'

  def test_required(self) -> None:
    assert Input(required=True).render_attrs() == 'required'

  def test_size(self) -> None:
    assert Input(size="foo").render_attrs() == 'size="foo"'

  def test_src(self) -> None:
    assert Input(src='www.foo.bar/baz/?quux="1"').render_attrs() == 'src="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_step(self) -> None:
    assert Input(step="foo").render_attrs() == 'step="foo"'

  def test_type(self) -> None:
    assert Input(type="button").render_attrs() == 'type="button"'

  def test_value(self) -> None:
    assert Input(value="foo").render_attrs() == 'value="foo"'

  def test_width(self) -> None:
    assert Input(width="foo").render_attrs() == 'width="foo"'

class TestInsAttrs():
  def test_cite(self) -> None:
    assert Ins(cite='www.foo.bar/baz/?quux="1"').render_attrs() == 'cite="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_datetime(self) -> None:
    assert Ins(datetime="foo").render_attrs() == 'datetime="foo"'

class TestLabelAttrs():
  def test_for_(self) -> None:
    assert Label(for_="foo").render_attrs() == 'for="foo"'

class TestLiAttrs():
  def test_value(self) -> None:
    assert Li(value="foo").render_attrs() == 'value="foo"'

class TestLinkAttrs():
  def test_as_(self) -> None:
    assert Link(as_="foo").render_attrs() == 'as="foo"'

  def test_crossorigin(self) -> None:
    assert Link(crossorigin="anonymous").render_attrs() == 'crossorigin="anonymous"'

  def test_fetchpriority(self) -> None:
    assert Link(fetchpriority="foo").render_attrs() == 'fetchpriority="foo"'

  def test_href(self) -> None:
    assert Link(href='www.foo.bar/baz/?quux="1"').render_attrs() == 'href="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_hreflang(self) -> None:
    assert Link(hreflang="foo").render_attrs() == 'hreflang="foo"'

  def test_imagesizes(self) -> None:
    assert Link(imagesizes="foo").render_attrs() == 'imagesizes="foo"'

  def test_imagesrcset(self) -> None:
    assert Link(imagesrcset='www.foo.bar/baz/?quux="1"').render_attrs() == 'imagesrcset="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_integrity(self) -> None:
    assert Link(integrity="foo").render_attrs() == 'integrity="foo"'

  def test_media(self) -> None:
    assert Link(media="foo").render_attrs() == 'media="foo"'

  def test_referrerpolicy(self) -> None:
    assert Link(referrerpolicy="no-referrer").render_attrs() == 'referrerpolicy="no-referrer"'

  def test_rel(self) -> None:
    assert Link(rel="alternate").render_attrs() == 'rel="alternate"'

  def test_sizes(self) -> None:
    assert Link(sizes="foo").render_attrs() == 'sizes="foo"'

  def test_type(self) -> None:
    assert Link(type="foo").render_attrs() == 'type="foo"'

class TestMapAttrs():
  def test_name(self) -> None:
    assert Map(name="foo").render_attrs() == 'name="foo"'

class TestMetaAttrs():
  def test_charset(self) -> None:
    assert Meta(charset="foo").render_attrs() == 'charset="foo"'

  def test_content(self) -> None:
    assert Meta(content="foo").render_attrs() == 'content="foo"'

  def test_http_equiv(self) -> None:
    assert Meta(http_equiv="content-security-policy").render_attrs() == 'http-equiv="content-security-policy"'

  def test_name(self) -> None:
    assert Meta(name="application-name").render_attrs() == 'name="application-name"'

class TestMeterAttrs():
  def test_form(self) -> None:
    assert Meter(form="foo").render_attrs() == 'form="foo"'

  def test_high(self) -> None:
    assert Meter(high="foo").render_attrs() == 'high="foo"'

  def test_low(self) -> None:
    assert Meter(low="foo").render_attrs() == 'low="foo"'

  def test_max(self) -> None:
    assert Meter(max="foo").render_attrs() == 'max="foo"'

  def test_min(self) -> None:
    assert Meter(min="foo").render_attrs() == 'min="foo"'

  def test_optimum(self) -> None:
    assert Meter(optimum="foo").render_attrs() == 'optimum="foo"'

  def test_value(self) -> None:
    assert Meter(value="foo").render_attrs() == 'value="foo"'

class TestObjectAttrs():
  def test_data(self) -> None:
    assert Object(data='www.foo.bar/baz/?quux="1"').render_attrs() == 'data="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_form(self) -> None:
    assert Object(form="foo").render_attrs() == 'form="foo"'

  def test_height(self) -> None:
    assert Object(height="foo").render_attrs() == 'height="foo"'

  def test_name(self) -> None:
    assert Object(name="foo").render_attrs() == 'name="foo"'

  def test_type(self) -> None:
    assert Object(type="foo").render_attrs() == 'type="foo"'

  def test_width(self) -> None:
    assert Object(width="foo").render_attrs() == 'width="foo"'

class TestOlAttrs():
  def test_reversed(self) -> None:
    assert Ol(reversed=True).render_attrs() == 'reversed'

  def test_start(self) -> None:
    assert Ol(start="foo").render_attrs() == 'start="foo"'

  def test_type(self) -> None:
    assert Ol(type="1").render_attrs() == 'type="1"'

class TestOptgroupAttrs():
  def test_disabled(self) -> None:
    assert Optgroup(disabled=True).render_attrs() == 'disabled'

  def test_label(self) -> None:
    assert Optgroup(label="foo").render_attrs() == 'label="foo"'

class TestOptionAttrs():
  def test_disabled(self) -> None:
    assert Option(disabled=True).render_attrs() == 'disabled'

  def test_label(self) -> None:
    assert Option(label="foo").render_attrs() == 'label="foo"'

  def test_selected(self) -> None:
    assert Option(selected=True).render_attrs() == 'selected'

  def test_value(self) -> None:
    assert Option(value="foo").render_attrs() == 'value="foo"'

class TestOutputAttrs():
  def test_for_(self) -> None:
    assert Output(for_="foo").render_attrs() == 'for="foo"'

  def test_form(self) -> None:
    assert Output(form="foo").render_attrs() == 'form="foo"'

  def test_name(self) -> None:
    assert Output(name="foo").render_attrs() == 'name="foo"'

class TestProgressAttrs():
  def test_max(self) -> None:
    assert Progress(max="foo").render_attrs() == 'max="foo"'

  def test_value(self) -> None:
    assert Progress(value="foo").render_attrs() == 'value="foo"'

class TestQAttrs():
  def test_cite(self) -> None:
    assert Q(cite='www.foo.bar/baz/?quux="1"').render_attrs() == 'cite="www.foo.bar/baz/?quux=&quot;1&quot;"'

class TestScriptAttrs():
  def test_async_(self) -> None:
    assert Script(async_=True).render_attrs() == 'async'

  def test_crossorigin(self) -> None:
    assert Script(crossorigin="anonymous").render_attrs() == 'crossorigin="anonymous"'

  def test_defer(self) -> None:
    assert Script(defer=True).render_attrs() == 'defer'

  def test_fetchpriority(self) -> None:
    assert Script(fetchpriority="foo").render_attrs() == 'fetchpriority="foo"'

  def test_integrity(self) -> None:
    assert Script(integrity="foo").render_attrs() == 'integrity="foo"'

  def test_nomodule(self) -> None:
    assert Script(nomodule=True).render_attrs() == 'nomodule'

  def test_nonce(self) -> None:
    assert Script(nonce="foo").render_attrs() == 'nonce="foo"'

  def test_referrerpolicy(self) -> None:
    assert Script(referrerpolicy="no-referrer").render_attrs() == 'referrerpolicy="no-referrer"'

  def test_src(self) -> None:
    assert Script(src='www.foo.bar/baz/?quux="1"').render_attrs() == 'src="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_type(self) -> None:
    assert Script(type="foo").render_attrs() == 'type="foo"'

class TestSelectAttrs():
  def test_autocomplete(self) -> None:
    assert Select(autocomplete="additional-name").render_attrs() == 'autocomplete="additional-name"'

  def test_autofocus(self) -> None:
    assert Select(autofocus=True).render_attrs() == 'autofocus'

  def test_disabled(self) -> None:
    assert Select(disabled=True).render_attrs() == 'disabled'

  def test_form(self) -> None:
    assert Select(form="foo").render_attrs() == 'form="foo"'

  def test_multiple(self) -> None:
    assert Select(multiple=True).render_attrs() == 'multiple'

  def test_name(self) -> None:
    assert Select(name="foo").render_attrs() == 'name="foo"'

  def test_required(self) -> None:
    assert Select(required=True).render_attrs() == 'required'

  def test_size(self) -> None:
    assert Select(size="foo").render_attrs() == 'size="foo"'

class TestSlotAttrs():
  def test_name(self) -> None:
    assert Slot(name="foo").render_attrs() == 'name="foo"'

class TestSourceAttrs():
  def test_height(self) -> None:
    assert Source(height="foo").render_attrs() == 'height="foo"'

  def test_media(self) -> None:
    assert Source(media="foo").render_attrs() == 'media="foo"'

  def test_sizes(self) -> None:
    assert Source(sizes="foo").render_attrs() == 'sizes="foo"'

  def test_src(self) -> None:
    assert Source(src='www.foo.bar/baz/?quux="1"').render_attrs() == 'src="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_srcset(self) -> None:
    assert Source(srcset='www.foo.bar/baz/?quux="1"').render_attrs() == 'srcset="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_type(self) -> None:
    assert Source(type="foo").render_attrs() == 'type="foo"'

  def test_width(self) -> None:
    assert Source(width="foo").render_attrs() == 'width="foo"'

class TestStyleAttrs():
  def test_blocking(self) -> None:
    assert Style(blocking="foo").render_attrs() == 'blocking="foo"'

  def test_media(self) -> None:
    assert Style(media="foo").render_attrs() == 'media="foo"'

  def test_nonce(self) -> None:
    assert Style(nonce="foo").render_attrs() == 'nonce="foo"'

  def test_title(self) -> None:
    assert Style(title="foo").render_attrs() == 'title="foo"'

class TestTdAttrs():
  def test_colspan(self) -> None:
    assert Td(colspan="foo").render_attrs() == 'colspan="foo"'

  def test_headers(self) -> None:
    assert Td(headers="foo").render_attrs() == 'headers="foo"'

  def test_rowspan(self) -> None:
    assert Td(rowspan="foo").render_attrs() == 'rowspan="foo"'

class TestTextareaAttrs():
  def test_autocomplete(self) -> None:
    assert Textarea(autocomplete="additional-name").render_attrs() == 'autocomplete="additional-name"'

  def test_autofocus(self) -> None:
    assert Textarea(autofocus=True).render_attrs() == 'autofocus'

  def test_cols(self) -> None:
    assert Textarea(cols="foo").render_attrs() == 'cols="foo"'

  def test_dirname(self) -> None:
    assert Textarea(dirname="foo").render_attrs() == 'dirname="foo"'

  def test_disabled(self) -> None:
    assert Textarea(disabled=True).render_attrs() == 'disabled'

  def test_form(self) -> None:
    assert Textarea(form="foo").render_attrs() == 'form="foo"'

  def test_maxlength(self) -> None:
    assert Textarea(maxlength="foo").render_attrs() == 'maxlength="foo"'

  def test_minlength(self) -> None:
    assert Textarea(minlength="foo").render_attrs() == 'minlength="foo"'

  def test_name(self) -> None:
    assert Textarea(name="foo").render_attrs() == 'name="foo"'

  def test_placeholder(self) -> None:
    assert Textarea(placeholder="foo").render_attrs() == 'placeholder="foo"'

  def test_readonly(self) -> None:
    assert Textarea(readonly=True).render_attrs() == 'readonly'

  def test_required(self) -> None:
    assert Textarea(required=True).render_attrs() == 'required'

  def test_rows(self) -> None:
    assert Textarea(rows="foo").render_attrs() == 'rows="foo"'

  def test_spellcheck(self) -> None:
    assert Textarea(spellcheck="default").render_attrs() == 'spellcheck="default"'

  def test_wrap(self) -> None:
    assert Textarea(wrap="hard").render_attrs() == 'wrap="hard"'

class TestThAttrs():
  def test_abbr(self) -> None:
    assert Th(abbr="foo").render_attrs() == 'abbr="foo"'

  def test_colspan(self) -> None:
    assert Th(colspan="foo").render_attrs() == 'colspan="foo"'

  def test_headers(self) -> None:
    assert Th(headers="foo").render_attrs() == 'headers="foo"'

  def test_rowspan(self) -> None:
    assert Th(rowspan="foo").render_attrs() == 'rowspan="foo"'

  def test_scope(self) -> None:
    assert Th(scope="col").render_attrs() == 'scope="col"'

class TestTimeAttrs():
  def test_datetime(self) -> None:
    assert Time(datetime="foo").render_attrs() == 'datetime="foo"'

class TestTrackAttrs():
  def test_default(self) -> None:
    assert Track(default=True).render_attrs() == 'default'

  def test_kind(self) -> None:
    assert Track(kind="captions").render_attrs() == 'kind="captions"'

  def test_label(self) -> None:
    assert Track(label="foo").render_attrs() == 'label="foo"'

  def test_src(self) -> None:
    assert Track(src='www.foo.bar/baz/?quux="1"').render_attrs() == 'src="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_srclang(self) -> None:
    assert Track(srclang="foo").render_attrs() == 'srclang="foo"'

class TestVideoAttrs():
  def test_autoplay(self) -> None:
    assert Video(autoplay=True).render_attrs() == 'autoplay'

  def test_controls(self) -> None:
    assert Video(controls=True).render_attrs() == 'controls'

  def test_crossorigin(self) -> None:
    assert Video(crossorigin="anonymous").render_attrs() == 'crossorigin="anonymous"'

  def test_disableremoteplayback(self) -> None:
    assert Video(disableremoteplayback=True).render_attrs() == 'disableremoteplayback'

  def test_loop(self) -> None:
    assert Video(loop=True).render_attrs() == 'loop'

  def test_muted(self) -> None:
    assert Video(muted=True).render_attrs() == 'muted'

  def test_playsinline(self) -> None:
    assert Video(playsinline=True).render_attrs() == 'playsinline'

  def test_poster(self) -> None:
    assert Video(poster='www.foo.bar/baz/?quux="1"').render_attrs() == 'poster="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_preload(self) -> None:
    assert Video(preload="auto").render_attrs() == 'preload="auto"'

  def test_src(self) -> None:
    assert Video(src='www.foo.bar/baz/?quux="1"').render_attrs() == 'src="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_width(self) -> None:
    assert Video(width="foo").render_attrs() == 'width="foo"'

