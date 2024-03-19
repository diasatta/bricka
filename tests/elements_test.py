from bricka.elements import *

class TestElements():
  #region A
  def test_a(self) -> None:
    assert A().render() == "<a></a>"

  def test_abbr(self) -> None:
    assert Abbr().render() == "<abbr></abbr>"

  def test_address(self) -> None:
    assert Address().render() == "<address></address>"

  def test_area(self) -> None:
    assert Area().render() == "<area>"

  def test_article(self) -> None:
    assert Article().render() == "<article></article>"

  def test_aside(self) -> None:
    assert Aside().render() == "<aside></aside>"

  def test_audio(self) -> None:
    assert Audio().render() == "<audio></audio>"

  #endregion
  #region B
  def test_b(self) -> None:
    assert B().render() == "<b></b>"

  def test_base(self) -> None:
    assert Base().render() == "<base>"

  def test_bdi(self) -> None:
    assert Bdi().render() == "<bdi></bdi>"

  def test_bdo(self) -> None:
    assert Bdo().render() == "<bdo></bdo>"

  def test_blockquote(self) -> None:
    assert Blockquote().render() == "<blockquote></blockquote>"

  def test_body(self) -> None:
    assert Body().render() == "<body></body>"

  def test_br(self) -> None:
    assert Br().render() == "<br>"

  def test_button(self) -> None:
    assert Button().render() == "<button></button>"

  #endregion
  #region C
  def test_canvas(self) -> None:
    assert Canvas().render() == "<canvas></canvas>"

  def test_caption(self) -> None:
    assert Caption().render() == "<caption></caption>"

  def test_cite(self) -> None:
    assert Cite().render() == "<cite></cite>"

  def test_code(self) -> None:
    assert Code().render() == "<code></code>"

  def test_col(self) -> None:
    assert Col().render() == "<col>"

  def test_colgroup(self) -> None:
    assert Colgroup().render() == "<colgroup></colgroup>"

  # def test_comment(self) -> None:
  #   assert Comment("This is a comment!").render() == "<!--This is a comment!-->"

  #endregion
  #region D
  def test_data(self) -> None:
    assert Data().render() == "<data></data>"

  def test_datalist(self) -> None:
    assert Datalist().render() == "<datalist></datalist>"

  def test_dd(self) -> None:
    assert Dd().render() == "<dd></dd>"

  def test_del(self) -> None:
    assert Del().render() == "<del></del>"

  def test_details(self) -> None:
    assert Details().render() == "<details></details>"

  def test_dfn(self) -> None:
    assert Dfn().render() == "<dfn></dfn>"

  def test_dialog(self) -> None:
    assert Dialog().render() == "<dialog></dialog>"

  def test_div(self) -> None:
    assert Div().render() == "<div></div>"

  def test_dl(self) -> None:
    assert Dl().render() == "<dl></dl>"

  def test_dt(self) -> None:
    assert Dt().render() == "<dt></dt>"

  #endregion
  #region E
  def test_em(self) -> None:
    assert Em().render() == "<em></em>"

  def test_embed(self) -> None:
    assert Embed().render() == "<embed>"

  #endregion
  #region F
  def test_fieldset(self) -> None:
    assert Fieldset().render() == "<fieldset></fieldset>"

  def test_figcaption(self) -> None:
    assert Figcaption().render() == "<figcaption></figcaption>"

  def test_figure(self) -> None:
    assert Figure().render() == "<figure></figure>"

  def test_footer(self) -> None:
    assert Footer().render() == "<footer></footer>"

  def test_form(self) -> None:
    assert Form().render() == "<form></form>"

  #endregion
  #region H
  def test_h1(self) -> None:
    assert H1().render() == "<h1></h1>"

  def test_h2(self) -> None:
    assert H2().render() == "<h2></h2>"

  def test_h3(self) -> None:
    assert H3().render() == "<h3></h3>"

  def test_h4(self) -> None:
    assert H4().render() == "<h4></h4>"

  def test_h5(self) -> None:
    assert H5().render() == "<h5></h5>"

  def test_h6(self) -> None:
    assert H6().render() == "<h6></h6>"

  def test_head(self) -> None:
    assert Head().render() == "<head></head>"

  def test_header(self) -> None:
    assert Header().render() == "<header></header>"

  def test_hgroup(self) -> None:
    assert Hgroup().render() == "<hgroup></hgroup>"

  def test_hr(self) -> None:
    assert Hr().render() == "<hr>"

  def test_html(self) -> None:
    assert Html().render() == "<!DOCTYPE html>\n<html></html>"

  #endregion
  #region I
  def test_i(self) -> None:
    assert I().render() == "<i></i>"

  def test_iframe(self) -> None:
    assert Iframe().render() == "<iframe></iframe>"

  def test_img(self) -> None:
    assert Img().render() == "<img>"

  def test_input(self) -> None:
    assert Input().render() == "<input>"

  def test_ins(self) -> None:
    assert Ins().render() == "<ins></ins>"

  #endregion
  #region K
  def test_kbd(self) -> None:
    assert Kbd().render() == "<kbd></kbd>"

  #endregion
  #region L
  def test_label(self) -> None:
    assert Label().render() == "<label></label>"

  def test_legend(self) -> None:
    assert Legend().render() == "<legend></legend>"

  def test_li(self) -> None:
    assert Li().render() == "<li></li>"

  def test_link(self) -> None:
    assert Link().render() == "<link>"

  #endregion
  #region M
  def test_main(self) -> None:
    assert Main().render() == "<main></main>"

  def test_map(self) -> None:
    assert Map().render() == "<map></map>"

  def test_mark(self) -> None:
    assert Mark().render() == "<mark></mark>"

  def test_menu(self) -> None:
    assert Menu().render() == "<menu></menu>"

  def test_meta(self) -> None:
    assert Meta().render() == "<meta>"

  def test_meter(self) -> None:
    assert Meter().render() == "<meter></meter>"

  #endregion
  #region N
  def test_nav(self) -> None:
    assert Nav().render() == "<nav></nav>"

  def test_noscript(self) -> None:
    assert Noscript().render() == "<noscript></noscript>"

  #endregion
  #region O
  def test_object(self) -> None:
    assert Object().render() == "<object></object>"

  def test_ol(self) -> None:
    assert Ol().render() == "<ol></ol>"

  def test_optgroup(self) -> None:
    assert Optgroup().render() == "<optgroup></optgroup>"

  def test_option(self) -> None:
    assert Option().render() == "<option></option>"

  def test_output(self) -> None:
    assert Output().render() == "<output></output>"

  #endregion
  #region P
  def test_p(self) -> None:
    assert P().render() == "<p></p>"

  def test_picture(self) -> None:
    assert Picture().render() == "<picture></picture>"

  def test_pre(self) -> None:
    assert Pre().render() == "<pre></pre>"

  def test_progress(self) -> None:
    assert Progress().render() == "<progress></progress>"

  #endregion
  #region Q
  def test_q(self) -> None:
    assert Q().render() == "<q></q>"

  #endregion
  #region R
  def test_rp(self) -> None:
    assert Rp().render() == "<rp></rp>"

  def test_rt(self) -> None:
    assert Rt().render() == "<rt></rt>"

  def test_ruby(self) -> None:
    assert Ruby().render() == "<ruby></ruby>"

  #endregion
  #region S
  def test_s(self) -> None:
    assert S().render() == "<s></s>"

  def test_samp(self) -> None:
    assert Samp().render() == "<samp></samp>"

  def test_script(self) -> None:
    assert Script().render() == "<script></script>"

  def test_section(self) -> None:
    assert Section().render() == "<section></section>"

  def test_select(self) -> None:
    assert Select().render() == "<select></select>"

  def test_slot(self) -> None:
    assert Slot().render() == "<slot></slot>"

  def test_small(self) -> None:
    assert Small().render() == "<small></small>"

  def test_source(self) -> None:
    assert Source().render() == "<source>"

  def test_span(self) -> None:
    assert Span().render() == "<span></span>"

  def test_strong(self) -> None:
    assert Strong().render() == "<strong></strong>"

  def test_style(self) -> None:
    assert Style().render() == "<style></style>"

  def test_sub(self) -> None:
    assert Sub().render() == "<sub></sub>"

  def test_summary(self) -> None:
    assert Summary().render() == "<summary></summary>"

  def test_sup(self) -> None:
    assert Sup().render() == "<sup></sup>"

  def test_svg(self) -> None:
    assert Svg().render() == "<svg></svg>"

  #endregion
  #region T
  def test_table(self) -> None:
    assert Table().render() == "<table></table>"

  def test_tbody(self) -> None:
    assert Tbody().render() == "<tbody></tbody>"

  def test_td(self) -> None:
    assert Td().render() == "<td></td>"

  def test_template(self) -> None:
    assert Template().render() == "<template></template>"

  def test_textarea(self) -> None:
    assert Textarea().render() == "<textarea></textarea>"

  def test_tfoot(self) -> None:
    assert Tfoot().render() == "<tfoot></tfoot>"

  def test_th(self) -> None:
    assert Th().render() == "<th></th>"

  def test_thead(self) -> None:
    assert Thead().render() == "<thead></thead>"

  def test_time(self) -> None:
    assert Time().render() == "<time></time>"

  def test_title(self) -> None:
    assert Title().render() == "<title></title>"

  def test_tr(self) -> None:
    assert Tr().render() == "<tr></tr>"

  def test_track(self) -> None:
    assert Track().render() == "<track>"

  #endregion
  #region U
  def test_u(self) -> None:
    assert U().render() == "<u></u>"

  def test_ul(self) -> None:
    assert Ul().render() == "<ul></ul>"

  #endregion
  #region V
  def test_var(self) -> None:
    assert Var().render() == "<var></var>"

  def test_video(self) -> None:
    assert Video().render() == "<video></video>"

  #endregion
  #region W
  def test_wbr(self) -> None:
    assert Wbr().render() == "<wbr>"

