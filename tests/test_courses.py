from playwright.sync_api import sync_playwright, expect, Page
import pytest

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state: Page):
    page = chromium_page_with_state
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text('Courses')

    courses_list_empty = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_list_empty).to_be_visible()
    expect(courses_list_empty).to_have_text('There is no results')

    courses_list_empty_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_list_empty_icon).to_be_visible()

    courses_list_empty_description = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(courses_list_empty_description).to_be_visible()
    expect(courses_list_empty_description).to_have_text(
        'Results from the load test pipeline will be displayed here')

    page.wait_for_timeout(5000)


@pytest.mark.regression
@pytest.mark.courses
def test_create_course(courses_list_page: CoursesListPage,
                       create_course_page: CreateCoursePage):
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()

    create_course_page.check_visible_image_upload_view(is_image_uploaded=False)
    create_course_page.check_visible_create_course_form(title="", estimated_time="", description="", max_score="0",
                                                        min_score="0")
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()

    create_course_page.upload_preview_image("./testdata/files/image.png")
    create_course_page.check_visible_image_upload_view()

    create_course_page.fill_create_course_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10"
    )

    create_course_page.click_create_course_button()

    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(title="Playwright",max_score="100",min_score="10",estimated_time="2 weeks",index=0)
