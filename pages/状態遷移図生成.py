import streamlit as st
from graphviz import Digraph

# アプリのタイトル
st.title("状態遷移図自動生成")

# 1. 状態数の入力（最大値を20に設定）
num_states = st.number_input("状態の数", min_value=2, max_value=20, step=1)

# 2. 各状態の名前を入力
states = []
for i in range(num_states):
    state_name = st.text_input(f"状態 {i + 1} の名前", key=f"state_{i}")
    states.append(state_name)

# 3. 各状態からの遷移先を選択
transitions = []

for i in range(num_states):
    from_state = states[i]
    # 遷移先の状態を選択
    transition_states = st.multiselect(f"{from_state} から遷移する状態を選択", states, key=f"transitions_{i}")
    
    # 遷移条件の入力 (複数行)
    for to_state in transition_states:
        if to_state != from_state:  # 自遷移は除外
            transition_condition = st.text_area(f"{from_state} から {to_state} への遷移条件", key=f"transition_{i}_{to_state}")
            if transition_condition:
                transitions.append((from_state, to_state, transition_condition))

# 4. 状態遷移図の作成
if st.button("状態遷移図を生成"):
    dot = Digraph(format="png")
    
    # ノード（状態）の追加
    for state in states:
        dot.node(state, state)

    # エッジ（遷移）の追加
    for (from_state, to_state, condition) in transitions:
        dot.edge(from_state, to_state, label=condition)

    # 生成した状態遷移図を表示
    st.graphviz_chart(dot)
