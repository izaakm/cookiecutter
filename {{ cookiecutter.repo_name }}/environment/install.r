# if (!requireNamespace("BiocManager", quietly = TRUE))
# install.packages("BiocManager")
# BiocManager::install("edgeR")

load_or_install_packages = function(list_of_packages) {

    new.packages <- list_of_packages[!(list_of_packages %in% installed.packages()[,"Package"])]
    if(length(new.packages)) {
        if (!requireNamespace("BiocManager", quietly = TRUE)) {
            install.packages("BiocManager", repos='http://cran.us.r-project.org')
        }
        # BiocManager::install(version = "3.10")
        # The install() function is provided by BiocManager. This is a
        # wrapper around install.packages, but with the repository
        # chosen according to the version of Bioconductor in use, rather
        # than to the version relevant at the time of the release of R.
        # https://bioconductor.org/install/
        BiocManager::install(new.packages)
    }
    # lapply(list_of_packages, require, character.only = TRUE)
    lapply(list_of_packages, require, character.only = TRUE)

}

l = c(
      "optparse"
     )

load_or_install_packages(l)

# END.
