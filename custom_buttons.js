survey.onCurrentPageChanging.add((survey, options) => {
  if (options.newCurrentPage.name == "AUT_cegla") {
    survey.addNavigationItem({
      id: "complete-AUT",
      title: "Zakończ AUT",
      action: () => {
        survey.currentPageNo = survey.getPageByName("AUT_patyk").num;
        survey.navigationBar.getActionById("complete-AUT").visible = false;
      },
      visibleIndex: 21,
      css: "nav-button",
      innerCss: "sd-btn",
    });
  } else if (options.oldCurrentPage.name == "AUT_patyk") {
    survey.navigationBar.getActionById("complete-AUT").visible = false;
  }
});
