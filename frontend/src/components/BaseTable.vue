
<template>
  <div class="vuetable-wrapper" :class="{'loading': loading}">
    <div class="loader"></div>
    <vuetable ref="vuetable"
      @vuetable:cell-clicked="emit"
      :api-mode="false"
      :fields="fields"
      :per-page="perPage"
      :data-manager="dataManager"
      pagination-path="pagination"
      :css="css.table"
      wrapper-class="vuetable-wrapper"
      @vuetable:pagination-data="onPaginationData"
    >
    <slot slot="custom-actions" slot-scope="props" v-bind:parentProps="props"></slot>
    </vuetable>
    <vuetable-pagination ref="pagination"
      @vuetable-pagination:change-page="onChangePage"
      :css="css.pagination"
    ></vuetable-pagination>
  </div>
</template>
<script>
import Vuetable from 'vuetable-2/src/components/Vuetable'
import VuetablePagination from 'vuetable-2/src/components/VuetablePagination'
import CssForBootstrap4 from './css.js'
import _ from "lodash";

export default {
	data() {
		return {
      perPage: 10,
      css: CssForBootstrap4
		}
	},
	watch: {
    data() {
      this.$refs.vuetable.refresh();
    }
  },
  components: {
    Vuetable,
    VuetablePagination
  },
  props: {
    data: Array,
    fields: Array,
    loading: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    onPaginationData(paginationData) {
      this.$refs.pagination.setPaginationData(paginationData);
    },
    onChangePage(page) {
      this.$refs.vuetable.changePage(page);
    },
    dataManager(sortOrder, pagination) {
      if (this.data.length < 1) return;

      let local = this.data;

      // sortOrder can be empty, so we have to check for that as well
      if (sortOrder.length > 0) {
        // console.log("orderBy:", sortOrder[0].sortField, sortOrder[0].direction);
        local = _.orderBy(
          local,
          sortOrder[0].sortField,
          sortOrder[0].direction
        );
      }

      pagination = this.$refs.vuetable.makePagination(
        local.length,
        this.perPage
      );
      // console.log('pagination:', pagination)
      let from = pagination.from - 1;
      let to = from + this.perPage;

      return {
        pagination: pagination,
        data: _.slice(local, from, to)
      };
    },
    editAction(a,b) {
      console.log("slot actions: on-click", a.name);
      console.log("slot actions: on-click", b.name);

    },
    emit(obj, a) {
      this.$emit('vuetable:cell-clicked', obj, a);
    }
  }
}
</script>

<style scoped>
button.ui.button {
  padding: 8px 3px 8px 10px;
	margin-top: 1px;
	margin-bottom: 1px;
}

.vuetable-wrapper {
    position: relative;
    opacity: 1;
}
.loader {
    /* visibility: hidden; */
    opacity: 0;
    transition: opacity 0.3s linear;
    background: url('https://i.gifer.com/ZZ5H.gif') no-repeat bottom center;
    width: 200px;
    height: 30px;
    font-size: 1em;
    text-align: center;
    margin-left: -100px;
    letter-spacing: 4px;
    color: #3E97F6;
    position: absolute;
    top: 160px;
    left: 50%;
    background-size: contain;
}
.loading .loader {
    visibility: visible;
    opacity: 1;
    z-index: 100;
}
.loading .vuetable{
    opacity:0.3;
    filter: alpha(opacity=30); /* IE8 and earlier */
}
</style>