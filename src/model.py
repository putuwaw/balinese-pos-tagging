import streamlit as st
import pandas as pd

st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
)

st.header("Balinese POS Tagging")
st.write('''
Conditional Random Field (CRF) can be used for POS (Part of Speech) tagging using probabilistic approach. The prediction for a word or token depends not only on its own features (like the word itself) but also on the context around it (such as the POS tags of neighboring words).
''')

st.subheader("Dataset")
st.write(
    "Dataset for this model were taken from previous research by (Bimantara et al, 2024) which contains teks in balinese with its POS Tags.")
st.write("Dataset preview:")

original_dataset = 'datasets/original.csv' 
original_df = pd.read_csv(original_dataset)

st.dataframe(original_df.head(10))

st.write("First, we need to adjust the tags of the data to the specified tags.")
st.write("Modified tags:")

modified_dataset = 'datasets\modified_tags.csv' 
modified_df = pd.read_csv(modified_dataset)

st.dataframe(modified_df.head(10))

st.write('''
         Before we can feed the data for training, first we need to group each word into a sentence based on its senteceId
         ''')
st.code('''
        pos_tag_df = pd.read_csv('/content/drive/MyDrive/Datasets/all_Tag.csv')
        pos_tag_df

        import re

        def remove_punctuation(word):
            cleaned_word = re.sub(r'[^\w\s-]', '', word)
            return cleaned_word if cleaned_word else None

        grouped_corpus = pos_tag_df.groupby(['StoryID', 'SentenceID']).apply(
            lambda x: [(word, pos) for word, pos in zip(
                x['Word'].apply(remove_punctuation), x['POS Tag']
            ) if word is not None]
        ).reset_index(name='tagged_text')
        ''')

st.write("it will produce tagged_text with '(word, tag)' format:")

final_dataset = 'datasets/dataset.csv' 
final_df = pd.read_csv(final_dataset)

st.dataframe(final_df.head(10))

st.subheader("Feature Extraction")
st.write("We need to extract feature of each word for training")
st.code('''
        def word_features(sentence, i):
        word = sentence[i][0]
        features = {
            'word': word,
            'is_first': i == 0,
            'is_last': i == len(sentence) - 1,
            'is_capitalized': word[0].upper() == word[0],
            'is_all_caps': word.upper() == word,
            'is_all_lower': word.lower() == word,
            'prefix-1': word[0],
            'prefix-2': word[:2],
            'prefix-3': word[:3],
            'suffix-1': word[-1],
            'suffix-2': word[-2:],
            'suffix-3': word[-3:],
            'prev_word': '' if i == 0 else sentence[i-1][0],
            'next_word': '' if i == len(sentence)-1 else sentence[i+1][0],
            'has_hyphen': '-' in word,
            'is_numeric': word.isdigit(),
            'capitals_inside': word[1:].lower() != word[1:],
            'word_shape': ''.join(['X' if c.isupper() else 'x' if c.islower() else 'd' if c.isdigit() else '-' for c in word]),
            'prev_word_is_capitalized': '' if i == 0 else sentence[i-1][0][0].isupper(),
        }
        return features
        ''')

st.subheader("Model Summary:")
st.image("https://www.researchgate.net/publication/366162819/figure/fig2/AS:11431281106381786@1670632077213/CRF-model-structure-diagram.png", width=500)

st.write("Training:")
st.code('''
        X = [[word_features(sentence, i) for i in range(len(sentence))] for sentence in corpus]
        y = [[tag for _, tag in sentence] for sentence in corpus]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        c1_values = [0.01, 0.1, 1.0]
        c2_values = [0.01, 0.1, 1.0]

        best_crf = None
        best_accuracy = 0.0

        for c1 in c1_values:
            for c2 in c2_values:
                print(f"Training model dengan c1={c1}, c2={c2}...")

                # Buat model CRF
                crf = sklearn_crfsuite.CRF(
                    algorithm='lbfgs',
                    c1=c1,
                    c2=c2,
                    max_iterations=100,
                    all_possible_transitions=True
                )

                crf.fit(X_train, y_train)

                y_pred = crf.predict(X_test)

                accuracy = metrics.flat_accuracy_score(y_test, y_pred)
                print(f"Accuracy untuk c1={c1}, c2={c2}: {accuracy:.4f}")

                if accuracy > best_accuracy:
                    best_accuracy = accuracy
                    best_crf = crf
                    joblib.dump(best_crf, "best_crf_model.pkl") 
                    print(f"Model baru disimpan dengan akurasi terbaik: {best_accuracy:.4f}")

        print(f"Model terbaik menggunakan c1={best_crf.c1}, c2={best_crf.c2} dengan akurasi: {best_accuracy:.4f}")
        ''')

st.subheader("Evaluation")
st.write("Model evaluation with accuracy score.")
st.image("evaluation.png")

st.subheader("Inference")
st.write("This function is used to predict tags from saved model")
st.code('''
        def predict_sentence_tags(crf_model, sentence):
            words = nltk.word_tokenize(sentence)
            features = [word_features(words, i) for i in range(len(words))]
            predicted_tags = crf_model.predict([features])[0]
            return list(zip(words, predicted_tags))
        ''')


