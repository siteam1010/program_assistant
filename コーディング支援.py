import streamlit as st

# タイトル
st.title("コーディング支援ツール")

# サイドバーで選択肢を表示
mode = st.sidebar.radio("モードを選択", ("制御コード生成", "宣言コード生成"))

# 制御コード生成の内容
if mode == "制御コード生成":
    st.header("制御コード生成")

    # セッションステートで表示内容を管理
    if "code_displayed" not in st.session_state:
        st.session_state.code_displayed = ""

    # 折りたたみ表示の管理
    if "expanders_open" not in st.session_state:
        st.session_state.expanders_open = {
            "if文": True,  # 初期状態で開く
            "if else文": True,  # 初期状態で開く
            "switch文": True,  # 初期状態で開く
            "while文": True,  # 初期状態で開く
            "for文": True,  # 初期状態で開く
        }

    # プログラム構造の表示
    # if文の参考プログラム
    if st.session_state.expanders_open["if文"]:
        with st.expander("if文"):
            condition = st.text_input("if文の条件を入力", key="if_condition")
            if_code = st.text_area("if文の処理を入力", key="if_code")
            comment = st.text_area("if文のコメントを入力", height=68, key="if_comment")  # 高さを68に変更
            if st.button("if文を表示"):
                st.session_state.code_displayed = f"""
/* {comment} */
if ({condition}) 
{{
    {if_code}
}}
"""

    # if else文の参考プログラム
    if st.session_state.expanders_open["if else文"]:
        with st.expander("if else文"):
            condition = st.text_input("if else文の条件を入力", key="if_else_condition")
            if_code = st.text_area("if文の処理を入力", key="if_else_code")
            if_comment = st.text_area("if文のコメントを入力", height=68, key="if_else_if_comment")  # if文のコメント入力エリア追加

            # else if文の数を入力
            num_else_if = st.number_input("else if文の数を入力", min_value=0, step=1, key="num_else_if")

            else_if_conditions = []
            else_if_codes = []
            else_if_comments = []

            for i in range(num_else_if):
                else_if_condition = st.text_input(f"else if {i+1}の条件を入力", key=f"else_if_condition_{i}")
                else_if_code = st.text_area(f"else if {i+1}の処理を入力", key=f"else_if_code_{i}")
                else_if_comment = st.text_area(f"else if {i+1}のコメントを入力", height=68, key=f"else_if_comment_{i}")  # 高さを68に変更
                else_if_conditions.append(else_if_condition)
                else_if_codes.append(else_if_code)
                else_if_comments.append(else_if_comment)

            else_code = st.text_area("else文の処理を入力", key="else_code")
            else_comment = st.text_area("else文のコメントを入力", height=68, key="else_comment")  # 高さを68に変更

            if st.button("if else文を表示"):
                else_if_code_str = ""
                for i in range(num_else_if):
                    else_if_code_str += f"""
/* {else_if_comments[i]} */
else if ({else_if_conditions[i]}) 
{{
    {else_if_codes[i]}
}}"""

                st.session_state.code_displayed = f"""
/* {if_comment} */
if ({condition}) 
{{
    {if_code}
}}{else_if_code_str} else 
{{
    {else_code}
/* {else_comment} */
}}
"""

    # switch文の参考プログラム
    if st.session_state.expanders_open["switch文"]:
        with st.expander("switch文"):
            condition = st.text_input("switch文の条件を入力", key="switch_condition")
            num_cases = st.number_input("caseの数を入力", min_value=1, step=1, key="switch_num_cases")

            cases = []
            case_comments = []
            for i in range(num_cases):
                case_value = st.text_input(f"case {i+1}の値を入力", key=f"case_value_{i}")
                case_code = st.text_area(f"case {i+1}の処理を入力", key=f"case_code_{i}")
                case_comment = st.text_area(f"case {i+1}のコメントを入力", height=68, key=f"case_comment_{i}")  # 高さを68に変更
                cases.append((case_value, case_code, case_comment))

            default_code = st.text_area("defaultの処理を入力", key="default_code")
            default_comment = st.text_area("defaultのコメントを入力", height=68, key="default_comment")  # 高さを68に変更

            if st.button("switch文を表示"):
                case_code_str = ""
                for case_value, case_code, case_comment in cases:
                    case_code_str += f"""
/* {case_comment} */
    case {case_value}: 
        {case_code}
        break;
"""
                st.session_state.code_displayed = f"""
/* {comment} */
switch ({condition}) 
{{
{case_code_str}
    default: 
        {default_code}
/* {default_comment} */
}}
"""

    # while文の参考プログラム
    if st.session_state.expanders_open["while文"]:
        with st.expander("while文"):
            condition = st.text_input("while文の条件を入力", key="while_condition")
            while_code = st.text_area("while文の処理を入力", key="while_code")
            comment = st.text_area("コメントを入力", height=68, key="while_comment")  # 高さを68に変更
            if st.button("while文を表示"):
                st.session_state.code_displayed = f"""
/* {comment} */
while ({condition}) 
{{
    {while_code}
}}
"""

    # for文の参考プログラム
    if st.session_state.expanders_open["for文"]:
        with st.expander("for文"):
            initialization = st.text_input("for文の初期化式を入力", key="for_initialization")
            condition = st.text_input("for文の条件式を入力", key="for_condition")
            increment = st.text_input("for文の増分式を入力", key="for_increment")
            for_code = st.text_area("for文の処理を入力", key="for_code")
            comment = st.text_area("コメントを入力", height=68, key="for_comment")  # 高さを68に変更

            if st.button("for文を表示"):
                st.session_state.code_displayed = f"""
/* {comment} */
for ({initialization}; {condition}; {increment}) 
{{
    {for_code}
}}
"""

    # リセットボタン
    if st.button("表示をリセット"):
        st.session_state.code_displayed = ""

    # 現在の表示を更新
    if st.session_state.code_displayed:
        st.code(st.session_state.code_displayed, language="c")

    # メモ入力スペースを表示
    st.subheader("メモ")
    memo = st.text_area("一時的なメモを入力", height=300)


# 宣言コード生成の内容
elif mode == "宣言コード生成":
    st.header("宣言コード生成")

    # セッションステートで表示内容を管理
    if "declaration_code_displayed" not in st.session_state:
        st.session_state.declaration_code_displayed = ""

    # 変数宣言部分
    with st.expander("変数宣言"):
        # 変数の型を選択
        var_type = st.selectbox("変数の型を選択", ("char", "int", "short", "float", "double"))

        # 符号有無を選択
        sign_option = st.radio("符号有無を選択", ("有（符号あり）", "無（unsigned）"))

        # 符号無が選択された場合、型の前に"unsigned"を追加
        if sign_option == "無（unsigned）":
            var_type = f"unsigned {var_type}"

        # アクセス修飾子を選択
        visibility_option = st.radio("アクセス修飾子を選択", ("public", "static"))

        # visibility_optionに応じて、staticまたはpublicを設定
        if visibility_option == "static":
            var_type = f"static {var_type}"

        var_name = st.text_input("変数名を入力")
        array_size = st.text_input("配列のサイズを入力（空白の場合は配列なし）")

        # 配列サイズが入力されていれば配列宣言
        if array_size:
            declaration = f"{var_type} {var_name}[{array_size}];"
        else:
            declaration = f"{var_type} {var_name};"

        # 変数宣言を表示
        if st.button("変数宣言を表示"):
            if var_type and var_name:
                st.session_state.declaration_code_displayed = declaration

    # 関数宣言の参考プログラム
    with st.expander("関数宣言"):
        # 戻り値の型を選択（最後にvoid）
        return_type = st.selectbox("関数の戻り値の型を選択", ("char", "int", "short", "float", "double", "void"))

        # 符号有無を選択
        sign_option = st.radio("符号有無を選択", ("有（符号あり）", "無（unsigned）"), key="function_sign_option")

        # 符号無が選択された場合、型の前に"unsigned"を追加
        if sign_option == "無（unsigned）":
            return_type = f"unsigned {return_type}"

        # アクセス修飾子を選択
        visibility_option = st.radio("アクセス修飾子を選択", ("public", "static"), key="function_visibility")

        # visibility_optionに応じて、staticまたはpublicを設定
        if visibility_option == "static":
            return_type = f"static {return_type}"

        func_name = st.text_input("関数名を入力")
        num_params = st.number_input("引数の数を入力", min_value=0, step=1)

        params = []
        for i in range(num_params):
            param_sign_option = st.radio(f"引数{i+1}の符号有無を選択", ("有（符号あり）", "無（unsigned）"),
            key=f"param_sign_option_{i}")
            param_type = st.selectbox(f"引数{i+1}の型を選択", ("char", "int", "short", "float", "double"), key=f"param_type_{i}")
            param_name = st.text_input(f"引数{i+1}の名前を入力", key=f"param_name_{i}")

            # 符号無が選択された場合、引数の型に"unsigned"を追加
            if param_sign_option == "無（unsigned）":
                param_type = f"unsigned {param_type}"

            params.append(f"{param_type} {param_name}")

        # 関数宣言を表示
        if st.button("関数宣言を表示"):
            # 引数が0の場合はvoidを使用
            if num_params == 0:
                declaration = f"{return_type} {func_name}(void);"
            else:
                params_str = ", ".join(params)
                declaration = f"{return_type} {func_name}({params_str});"
            st.session_state.declaration_code_displayed = declaration

    # リセットボタン
    if st.button("表示をリセット"):
        st.session_state.declaration_code_displayed = ""

    # 宣言コードの表示
    if st.session_state.declaration_code_displayed:
        st.code(st.session_state.declaration_code_displayed, language="c")

    # メモ入力スペースを表示
    st.subheader("メモ")
    memo = st.text_area("一時的なメモを入力", height=300)
