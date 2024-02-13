import docx2txt

job_description = docx2txt.process('S:\Programming Practice\Resume Scanner\Cook Sample.docx')
resume = docx2txt.process('S:\Programming Practice\Resume Scanner\Cook Applicant.docx')
content = [job_description, resume]

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
matrix = cv.fit_transform(content)

from sklearn.metrics.pairwise import cosine_similarity
similarity_matrix = cosine_similarity(matrix)

print("Applicant resume matches the sample resume by " + str(round(similarity_matrix[1][0]*100)) + "%")