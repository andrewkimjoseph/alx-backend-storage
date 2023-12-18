#!/usr/bin/env python3
""" Module for using PyMongo """


def top_students(mongo_collection):
    """ Returns all students sorted by average score"""
    # Retrieve all students from the collection
    all_students = list(mongo_collection.find())

    # Calculate the average score for each student
    for student in all_students:
        scores = student.get('scores', [])
        if scores:
            average_score = sum(score['score'] for score in scores) / len(scores)
            student['averageScore'] = average_score
        else:
            student['averageScore'] = 0  # Set default average score if no scores are available

    # Sort students based on average scores in descending order
    sorted_students = sorted(all_students, key=lambda x: x['averageScore'], reverse=True)

    return sorted_students
